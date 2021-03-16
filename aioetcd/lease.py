from __future__ import annotations

import typing
import asyncio
from dataclasses import dataclass

from ._rpc import rpc_pb2_grpc
from ._rpc import rpc_pb2
from aioetcd.common import ResponseHeader

if typing.TYPE_CHECKING:
    from aioetcd._rpc_stubs import lease
    from grpc.aio._channel import Channel  # type: ignore

_default_timeout = 5


@dataclass
class Lease:
    id: int
    ttl: int


@dataclass
class LeaseGrantResponse:
    header: ResponseHeader
    id: int
    """The lease ID for the granted lease."""
    ttl: int
    """The server chosen lease time-to-live in seconds."""
    error: str


@dataclass
class LeaseRevokeResponse:
    header: ResponseHeader


@dataclass
class LeaseStatus:
    id: int


@dataclass
class LeasesResponse:
    header: ResponseHeader
    leases: typing.List[LeaseStatus]


@dataclass
class KeepAliveResponse:
    header: ResponseHeader
    id: int
    """The lease ID from the keep alive request."""
    ttl: int
    """The new time-to-live for the lease."""


@dataclass
class TimeToLiveResponse:
    header: ResponseHeader
    id: int
    """The lease ID from the keep alive request."""
    ttl: int
    """The remaining TTL in seconds for the lease;
    the lease will expire in under TTL+1 seconds."""
    granted_ttl: int
    """The initial granted time in seconds upon lease creation/renewal."""
    keys: typing.List[bytes]
    """The list of keys attached to this lease."""


EtcdResponceCallback = typing.Callable[
    [KeepAliveResponse], typing.Awaitable[typing.Any]
]


class KeepAliveLease:
    """Context manager for Keep Alive Leases"""

    def __init__(
        self,
        client: LeaseApi,
        ttl: int,
        *,
        etcd_response_callback: typing.Optional[EtcdResponceCallback] = None,
    ):
        self.client = client
        self.ttl = ttl
        self._lease_id: typing.Optional[int] = None
        self.finisher = asyncio.Event()
        self._keep_alive_task: typing.Optional[asyncio.Task[None]] = None
        self._response_callback = etcd_response_callback

    async def _run_keep_alive_task(self) -> None:
        if self._lease_id is None:
            raise RuntimeError("Unknown lease")
        async for response in self.client.keep_alive(
            self._lease_id, self.ttl // 2, self.finisher
        ):
            if self._response_callback is not None:
                asyncio.get_event_loop().create_task(
                    self._response_callback(response)
                )

    async def __aenter__(self) -> KeepAliveLease:
        lease = await self.client.grant(self.ttl)
        self._lease_id = lease.id
        self.finisher = asyncio.Event()
        self._keep_alive_task = asyncio.get_event_loop().create_task(
            self._run_keep_alive_task()
        )
        return self

    async def __aexit__(self, *_: typing.Any, **__: typing.Any) -> None:
        self.finisher.set()
        if self._keep_alive_task and not self._keep_alive_task.done():
            self._keep_alive_task.cancel()
            await asyncio.wait([self._keep_alive_task])
        self._keep_alive_task = None
        if self._lease_id is not None:
            await self.client.revoke(self._lease_id)


async def _keep_alive_request_generator(
    id: int, period: int, finisher: typing.Optional[asyncio.Event] = None
) -> typing.AsyncGenerator[lease.LeaseKeepAliveRequest, None]:
    if finisher is None:
        finisher = asyncio.Event()
    while not finisher.is_set():
        yield rpc_pb2.LeaseKeepAliveRequest(ID=id)
        await asyncio.sleep(period)


class LeaseApi:
    def __init__(self, channel: Channel):
        self._lease_stub: lease.LeaseStub = typing.cast(
            lease.LeaseStub, rpc_pb2_grpc.LeaseStub(channel)  # type: ignore
        )

    async def grant(self, ttl: int, id: int = 0) -> LeaseGrantResponse:
        """Creates a lease which expires if the server does not receive
        a keepAlive within a given time to live period. All keys attached
        to the lease will be expired and deleted if the lease expires.
        Each expired key generates a delete event in the event history.

        :param ttl: the advisory time-to-live in seconds. Expired lease
            will return -1.
        :param id: the requested ID for the lease. If ID is set to 0,
            the lessor chooses an ID.
        """
        request = rpc_pb2.LeaseGrantRequest(TTL=ttl, ID=id)
        r = await self._lease_stub.LeaseGrant(request)
        return LeaseGrantResponse(
            header=ResponseHeader.from_protobuf(r.header),
            id=r.ID,
            ttl=r.TTL,
            error=r.error,
        )

    async def revoke(self, id: int) -> LeaseRevokeResponse:
        """Revokes a lease. All keys attached to the lease will expire and be deleted.

        :param id: the lease ID to revoke. When the ID is revoked, all
            associated keys will be deleted.
        """
        request = rpc_pb2.LeaseRevokeRequest(ID=id)
        r = await self._lease_stub.LeaseRevoke(request)
        return LeaseRevokeResponse(
            header=ResponseHeader.from_protobuf(r.header)
        )

    async def time_to_live(
        self, id: int, keys: bool = False
    ) -> TimeToLiveResponse:
        """Retrieves lease information

        :param id: the lease ID for the lease.
        :param keys: keys is true to query all the keys attached to this lease.
        """
        request = rpc_pb2.LeaseTimeToLiveRequest(ID=id, keys=keys)
        r = await self._lease_stub.LeaseTimeToLive(request)
        return TimeToLiveResponse(
            header=ResponseHeader.from_protobuf(r.header),
            id=r.ID,
            ttl=r.TTL,
            granted_ttl=r.grantedTTL,
            keys=[key for key in r.keys],
        )

    async def leases(self) -> LeasesResponse:
        """Lists all existing leases."""
        request = rpc_pb2.LeaseLeasesRequest()
        r = await self._lease_stub.LeaseLeases(request)
        return LeasesResponse(
            header=ResponseHeader.from_protobuf(r.header),
            leases=[LeaseStatus(id=lease.ID) for lease in r.leases],
        )

    def _keep_alive(
        self,
        request_iterator: typing.AsyncGenerator[
            lease.LeaseKeepAliveRequest, None
        ],
    ) -> typing.AsyncGenerator[lease.LeaseKeepAliveResponse, None]:
        return self._lease_stub.LeaseKeepAlive(request_iterator)

    async def keep_alive(
        self,
        id: int,
        period: int,
        finisher: typing.Optional[asyncio.Event] = None,
    ) -> typing.AsyncGenerator[KeepAliveResponse, None]:
        """Keeps the lease alive by streaming keep alive requests from the client
        to the server and streaming keep alive responses from the server to
        the client.

        :param id: the lease ID for the lease to keep alive.
        :param period: time in seconds between keepAlive requests
        :param finisher: the keepAlive requests will be sent until the
            finisher event is set. If not set, the requests will be sent
            infinitely
        """

        async for result in self._keep_alive(
            _keep_alive_request_generator(id, period, finisher)
        ):
            yield KeepAliveResponse(
                header=ResponseHeader.from_protobuf(result.header),
                id=result.ID,
                ttl=result.TTL,
            )

    def keep_alive_context(
        self,
        ttl: int,
        *,
        response_callback: typing.Optional[EtcdResponceCallback] = None,
    ) -> KeepAliveLease:
        """Keeps the lease alive by streaming keep alive requests from the client
        to the server and streaming keep alive responses from the server to
        the client.
        """
        return KeepAliveLease(
            self, ttl, etcd_response_callback=response_callback
        )

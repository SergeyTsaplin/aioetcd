from __future__ import annotations
import typing

from typing_extensions import Protocol

from grpc.aio._channel import Channel  # type: ignore

from aioetcd._rpc import rpc_pb2


class LeaseStub(Protocol):
    def __init__(self, channel: Channel):
        ...

    async def LeaseGrant(
        self,
        request: rpc_pb2.LeaseGrantRequest,
        timeout: typing.Optional[int] = None,
    ) -> rpc_pb2.LeaseGrantResponse:
        ...

    async def LeaseRevoke(
        self,
        request: rpc_pb2.LeaseRevokeRequest,
        timeout: typing.Optional[int] = None,
    ) -> rpc_pb2.LeaseRevokeResponse:
        ...

    async def LeaseTimeToLive(
        self,
        request: rpc_pb2.LeaseTimeToLiveRequest,
        timeout: typing.Optional[int] = None,
    ) -> rpc_pb2.LeaseTimeToLiveResponse:
        ...

    async def LeaseLeases(
        self,
        request: rpc_pb2.LeaseLeasesRequest,
        timeout: typing.Optional[int] = None,
    ) -> rpc_pb2.LeaseLeasesResponse:
        ...

    def LeaseKeepAlive(
        self,
        request_iterator: typing.AsyncGenerator[
            rpc_pb2.LeaseKeepAliveRequest, None
        ],
    ) -> typing.AsyncGenerator[rpc_pb2.LeaseKeepAliveResponse, None]:
        ...

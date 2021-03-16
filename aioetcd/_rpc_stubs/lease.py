from __future__ import annotations
import typing

from typing_extensions import Protocol

from grpc.aio._channel import Channel  # type: ignore

from .common import ResponseHeader


class LeassGrantRequest(Protocol):
    def __init__(self, TTL: int, ID: int):
        ...


class LeaseGrantResponse(Protocol):
    header: ResponseHeader
    ID: int
    TTL: int
    error: str


class LeaseRevokeRequest(Protocol):
    def __init__(self, ID: int):
        ...


class LeaseRevokeResponse(Protocol):
    header: ResponseHeader


class LeaseLeasesRequest(Protocol):
    def __init__(self) -> None:
        ...


class LeaseStatus(Protocol):
    ID: int


class LeaseLeasesResponse(Protocol):
    header: ResponseHeader
    leases: typing.List[LeaseStatus]


class LeaseTimeToLiveRequest(Protocol):
    def __init__(self, ID: int, keys: bool):
        ...


class LeaseTimeToLiveResponse(Protocol):
    header: ResponseHeader
    ID: int
    TTL: int
    grantedTTL: int
    keys: typing.List[bytes]


class LeaseKeepAliveResponse(Protocol):
    header: ResponseHeader
    ID: int
    TTL: int


class LeaseKeepAliveRequest(Protocol):
    def __init__(self, ID: int):
        ...


class LeaseStub(Protocol):
    def __init__(self, channel: Channel):
        ...

    async def LeaseGrant(
        request: LeassGrantRequest, timeout: typing.Optional[int] = None
    ) -> LeaseGrantResponse:
        ...

    async def LeaseRevoke(
        request: LeaseRevokeRequest, timeout: typing.Optional[int] = None
    ) -> LeaseRevokeResponse:
        ...

    async def LeaseTimeToLive(
        request: LeaseTimeToLiveRequest,
        timeout: typing.Optional[int] = None,
    ) -> LeaseTimeToLiveResponse:
        ...

    async def LeaseLeases(
        request: LeaseLeasesRequest, timeout: typing.Optional[int] = None
    ) -> LeaseLeasesResponse:
        ...

    def LeaseKeepAlive(
        self,
        request_iterator: typing.AsyncGenerator[LeaseKeepAliveRequest, None],
    ) -> typing.AsyncGenerator[LeaseKeepAliveResponse, None]:
        ...

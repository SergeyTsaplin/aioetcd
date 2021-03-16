from __future__ import annotations
import typing
from typing_extensions import Protocol

from grpc.aio._channel import Channel  # type: ignore

from .common import ResponseHeader


class CompactionRequest(Protocol):
    def __init__(self, *, revision: int, physical: bool):
        ...


class CompactionResponse(Protocol):
    header: ResponseHeader


class KeyValue(Protocol):
    key: bytes
    create_revision: int
    mod_revision: int
    version: int
    value: bytes
    lease: int

    def __init__(
        self,
        *,
        key: bytes,
        create_revision: int,
        mod_revision: int,
        version: int,
        value: bytes,
        lease: int,
    ):
        ...


class Compare(Protocol):
    def __init__(
        self,
        *,
        result: int,
        target: int,
        key: bytes,
        range_end: typing.Optional[bytes],
    ):
        ...


class RequestOp(Protocol):
    def __init__(
        self,
        *,
        request_range: typing.Optional[typing.Any] = None,
        request_put: typing.Optional[typing.Any] = None,
        request_delete_range: typing.Optional[typing.Any] = None,
        request_txn: typing.Optional[typing.Any] = None,
    ):
        ...


class RangeRequest(Protocol):
    def __init__(
        self,
        key: bytes,
        range_end: typing.Optional[bytes],
        limit: int,
        revision: int,
        sort_order: int,
        sort_target: int,
        serializable: bool,
        keys_only: bool,
        count_only: bool,
        min_mod_revision: typing.Optional[int],
        max_mod_revision: typing.Optional[int],
        min_create_revision: typing.Optional[int],
        max_create_revision: typing.Optional[int],
    ):
        ...


class PutRequest(Protocol):
    def __init__(
        self,
        key: bytes,
        value: bytes,
        lease: int,
        prev_kv: bool,
        ignore_value: bool,
        ignore_lease: bool,
    ):
        ...


class DeleteRangeRequest(Protocol):
    def __init__(
        self,
        key: bytes,
        range_end: bytes,
        prev_kv: bool,
    ):
        ...


class RangeResponse(Protocol):
    header: ResponseHeader
    kvs: typing.List[KeyValue]
    more: bool
    count: int


class PutResponse(Protocol):
    header: ResponseHeader
    prev_kv: typing.Optional[KeyValue]


class DeleteRangeResponse(Protocol):
    header: ResponseHeader
    deleted: int
    prev_kvs: typing.List[KeyValue]


class TxnResponse(Protocol):
    header: ResponseHeader
    succeeded: bool
    responses: typing.Sequence["ResponseOp"]


class TxnRequest(Protocol):
    def __init__(
        self,
        *,
        compare: typing.List[Compare],
        success: typing.List[RequestOp],
        failure: typing.List[RequestOp],
    ):
        ...


class ResponseOp(Protocol):
    response: typing.Union[
        RangeResponse, PutResponse, DeleteRangeResponse, TxnResponse
    ]
    response_range: typing.Optional[RangeResponse]
    response_put: typing.Optional[PutResponse]
    response_delete_range: typing.Optional[DeleteRangeResponse]
    response_txn: typing.Optional[TxnResponse]


class KVStub(Protocol):
    def __init__(self, channel: Channel):
        ...

    async def Range(self, request: RangeRequest) -> RangeResponse:
        ...

    async def Put(self, request: PutRequest) -> PutResponse:
        ...

    async def DeleteRange(
        self, request: DeleteRangeRequest
    ) -> DeleteRangeResponse:
        ...

    async def Txn(self, request: TxnRequest) -> TxnResponse:
        ...

    async def Compact(self, request: CompactionRequest) -> CompactionResponse:
        ...

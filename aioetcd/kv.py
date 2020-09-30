from __future__ import annotations
import typing
from dataclasses import dataclass, InitVar, field
from enum import IntEnum

from aioetcd.common import ResponseHeader


from ._rpc import rpc_pb2_grpc
from ._rpc import rpc_pb2


class EventType(IntEnum):
    PUT = 0
    DELETE = 1


class SortOrder(IntEnum):
    NONE = 0
    ASCEND = 1
    DESCEND = 2


class CompareResult(IntEnum):
    EQUAL = 0
    GREATER = 1
    LESS = 2
    NOT_EQUAL = 3


class CompareTarget(IntEnum):
    VERSION = 0
    CREATE = 1
    MOD = 2
    VALUE = 3
    LEASE = 4


class SortTarget(IntEnum):
    KEY = 0
    VERSION = 1
    CREATE = 2
    MOD = 3
    VALUE = 4


@dataclass
class KeyValue:
    key: bytes
    create_revision: int
    mod_revision: int
    version: int
    value: bytes
    lease: int

    @classmethod
    def from_protobuf(cls, pb_value) -> KeyValue:
        return KeyValue(
            key=pb_value.key,
            create_revision=pb_value.create_revision,
            mod_revision=pb_value.mod_revision,
            version=pb_value.version,
            value=pb_value.value,
            lease=pb_value.lease,
        )


@dataclass
class Event:
    type: EventType
    kv: typing.Optional[KeyValue]
    prev_kv: typing.Optional[KeyValue]


@dataclass
class CompareTargetUnion:
    version: typing.Optional[int] = None
    create_revision: typing.Optional[int] = None
    mod_revision: typing.Optional[int] = None
    value: typing.Optional[bytes] = None
    lease: typing.Optional[int] = None


@dataclass
class Compare:
    result: CompareResult
    target: CompareTarget
    key: bytes
    target_union: CompareTargetUnion
    range_end: bytes


@dataclass
class RangeResponse:
    header: ResponseHeader
    kvs: typing.List[KeyValue]
    more: bool
    count: int


@dataclass
class RangeRequest:
    _kv: rpc_pb2_grpc.KVStub = field(hash=False, compare=False, repr=False)
    key: bytes
    range_end: bytes
    limit: int
    revision: int
    sort_order: SortOrder
    sort_target: SortTarget
    serializable: bool
    keys_only: bool
    count_only: bool
    min_mod_revision: int
    max_mod_revision: int
    min_create_revision: int
    max_create_revision: int

    def as_protobuf(self) -> rpc_pb2.RangeRequest:
        return rpc_pb2.RangeRequest(
            key=self.key,
            range_end=self.range_end,
            limit=self.limit,
            revision=self.revision,
            sort_order=self.sort_order.value,
            sort_target=self.sort_target.value,
            serializable=self.serializable,
            keys_only=self.keys_only,
            count_only=self.count_only,
            min_mod_revision=self.min_mod_revision,
            max_mod_revision=self.max_mod_revision,
            min_create_revision=self.min_create_revision,
            max_create_revision=self.max_create_revision,
        )

    def __await__(self) -> RangeResponse:
        response = await self._kv.Range(self.as_protobuf())
        return RangeResponse(
            header=ResponseHeader.from_protobuf(response.header),
            kvs=[KeyValue.from_protobuf(kv) for kv in response.kvs],
            more=response.more,
            count=response.count,
        )


@dataclass
class PutResponse:
    header: ResponseHeader
    prev_kv: typing.Optional[KeyValue]


@dataclass
class PutRequest:
    key: bytes
    value: bytes
    lease: int
    prev_kv: bool
    ignore_value: bool
    ignore_lease: bool

    def __init__(self, kv, key, value, lease, prev_kv, ignore_value, ignore_lease):
        self.__kv = kv
        self.key = key
        self.value = value
        self.lease = lease
        self.prev_kv = prev_kv
        self.ignore_value = ignore_value
        self.ignore_lease = ignore_lease

    def as_protobuf(self) -> rpc_pb2.PutRequest:
        return rpc_pb2.PutRequest(
            key=self.key,
            value=self.value,
            lease=self.lease,
            prev_kv=self.prev_kv,
            ignore_value=self.ignore_value,
            ignore_lease=self.ignore_lease
        )

    def __await__(self) -> PutResponse:
        response = await self.__kv.Put(self.as_protobuf())
        return PutResponse(
            header=ResponseHeader.from_protobuf(response.header),
            prev_kv=response.prev_kv
        )


@dataclass
class DeleteRangeRequest:
    key: bytes
    range_end: bytes
    prev_kv: bool


@dataclass
class DeleteRangeResponse:
    header: ResponseHeader
    deleted: int
    prev_kvs: typing.List[KeyValue]


@dataclass
class TxnRequest:
    compare: typing.List[Compare]
    success: typing.List["RequestOp"]
    failure: typing.List["RequestOp"]


@dataclass
class RequestOp:
    request: typing.Union[
        RangeRequest, PutRequest, DeleteRangeRequest, TxnRequest
    ]


@dataclass
class TxnResponse:
    header: ResponseHeader
    succeeded: bool
    responses: typing.List["ResponseOp"]


@dataclass
class ResponseOp:
    response: typing.Union[
        RangeResponse, PutResponse, DeleteRangeResponse, TxnResponse
    ]


class KVApi:
    def __init__(self, channel):
        self._kv_stub = rpc_pb2_grpc.KVStub(channel=channel)

    def range(
        self,
        key: bytes,
        range_end: bytes,
        limit: int = 0,
        revision: int = 0,
        sort_order: SortOrder = SortOrder.NONE,
        sort_target: SortTarget = SortTarget.KEY,
        serializable: bool = False,
        keys_only: bool = False,
        count_only: bool = False,
        min_mod_revision: typing.Optional[int] = None,
        max_mod_revision: typing.Optional[int] = None,
        min_create_revision: typing.Optional[int] = None,
        max_create_revision: typing.Optional[int] = None,
        *,
        timeout: float = 0,
    ) -> RangeRequest:
        return RangeRequest(
            self._kv_stub, key, range_end, limit, revision, sort_order, sort_target, serializable,
            keys_only, count_only, min_mod_revision, max_mod_revision, min_create_revision, max_create_revision
        )

    def put(
        self,
        key: bytes,
        value: bytes,
        lease: int,
        prev_kv: bool,
        ignore_value: bool,
        ignore_lease: bool,
        *,
        timeout: float = 0,
    ) -> PutRequest:
        return PutRequest(self._kv_stub, key, value, lease, prev_kv, ignore_value, ignore_lease)

    async def delete_range(
        self, key: bytes, range_end: bytes, prev_kv: bool,
    ) -> DeleteRangeResponse:
        ...

    async def txn(
        self,
        compare: typing.Sequence[Compare],
        success: typing.Sequence[RequestOp],
        failure: typing.Sequence[RequestOp],
    ) -> TxnResponse:
        ...

    async def compact(self, revision: int, physical: bool) -> ResponseHeader:
        ...

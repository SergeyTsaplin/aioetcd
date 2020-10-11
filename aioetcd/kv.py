from __future__ import annotations
import typing
from dataclasses import dataclass, field
from enum import IntEnum
import abc

from aioetcd.common import ResponseHeader


from ._rpc import rpc_pb2_grpc
from ._rpc import rpc_pb2

if typing.TYPE_CHECKING:
    from aioetcd.client import Client


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


T = typing.TypeVar("T")


class EtcdResponse(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def from_protobuf(cls: typing.Type[T], pb_value, request) -> T:
        ...


class TxnOperation(abc.ABC):
    @abc.abstractmethod
    def as_txn_operation(self) -> rpc_pb2.RequestOp:
        ...


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

    def __post_init__(self):
        defined_count = (
            int(self.version is not None)
            + int(self.create_revision is not None)
            + int(self.mod_revision is not None)
            + int(self.value is not None)
            + int(self.lease is not None)
        )
        if defined_count > 1:
            raise ValueError(
                "Only one of the object parameters must be defined"
            )
        elif defined_count == 0:
            raise ValueError("One of the object parameters must be defined")

    def get_value(self, target: CompareTarget):
        if target == CompareTarget.VERSION:
            return {"version": self.version}
        elif target == CompareTarget.CREATE:
            return {"create_revision": self.create_revision}
        elif target == CompareTarget.MOD:
            return {"mod_revision": self.mod_revision}
        elif target == CompareTarget.VALUE:
            return {"value": self.value}
        elif target == CompareTarget.LEASE:
            return {"lease": self.lease}
        else:
            ValueError(f"Invalid target value: {target}")


@dataclass
class Compare:
    result: CompareResult
    target: CompareTarget
    key: bytes
    target_union: CompareTargetUnion
    range_end: typing.Optional[bytes] = None

    def as_protobuf(self):
        return rpc_pb2.Compare(
            result=self.result.value,
            target=self.target.value,
            key=self.key,
            range_end=self.range_end,
            **self.target_union.get_value(self.target),
        )


@dataclass
class RangeResponse(EtcdResponse):
    header: ResponseHeader
    kvs: typing.List[KeyValue]
    more: bool
    count: int

    @classmethod
    def from_protobuf(cls, pb_value, request: RangeRequest) -> RangeResponse:
        return RangeResponse(
            header=ResponseHeader.from_protobuf(pb_value.header),
            kvs=[KeyValue.from_protobuf(kv) for kv in pb_value.kvs],
            more=pb_value.more,
            count=pb_value.count,
        )


@dataclass(frozen=True)
class RangeRequest(TxnOperation):
    key: bytes
    range_end: typing.Optional[bytes]
    limit: int
    revision: int
    sort_order: SortOrder
    sort_target: SortTarget
    serializable: bool
    keys_only: bool
    count_only: bool
    min_mod_revision: typing.Optional[int]
    max_mod_revision: typing.Optional[int]
    min_create_revision: typing.Optional[int]
    max_create_revision: typing.Optional[int]
    _kv: typing.Optional[rpc_pb2_grpc.KVStub] = field(
        hash=False, compare=False, repr=False, default=None
    )

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

    def as_txn_operation(self) -> rpc_pb2.RequestOp:
        return rpc_pb2.RequestOp(request_range=self.as_protobuf())

    def __await__(self) -> RangeResponse:
        if self._kv is None:
            raise TypeError("RangeRequest is not awaitable")
        response = yield from self._kv.Range(self.as_protobuf()).__await__()
        return RangeResponse.from_protobuf(response, self)


@dataclass
class PutResponse(EtcdResponse):
    header: ResponseHeader
    prev_kv: typing.Optional[KeyValue]

    _key_name: typing.ClassVar = "response_put"

    @classmethod
    def from_protobuf(cls, pb_value, request: PutRequest) -> PutResponse:
        return PutResponse(
            header=ResponseHeader.from_protobuf(pb_value.header),
            prev_kv=pb_value.prev_kv,
        )


@dataclass(frozen=True)
class PutRequest(TxnOperation):
    key: bytes
    value: bytes
    lease: int
    prev_kv: bool
    ignore_value: bool
    ignore_lease: bool
    _kv: typing.Optional[rpc_pb2_grpc.KVStub] = field(
        hash=False, compare=False, repr=False, default=None
    )
    _response_cls: typing.ClassVar = PutResponse

    def as_protobuf(self) -> rpc_pb2.PutRequest:
        return rpc_pb2.PutRequest(
            key=self.key,
            value=self.value,
            lease=self.lease,
            prev_kv=self.prev_kv,
            ignore_value=self.ignore_value,
            ignore_lease=self.ignore_lease,
        )

    def as_txn_operation(self) -> rpc_pb2.RequestOp:
        return rpc_pb2.RequestOp(request_put=self.as_protobuf())

    def __await__(self) -> PutResponse:
        if self._kv is None:
            raise TypeError("RangeRequest is not awaitable")
        response = yield from self._kv.Put(self.as_protobuf()).__await__()
        return PutResponse.from_protobuf(response, self)


@dataclass
class DeleteRangeResponse(EtcdResponse):
    header: ResponseHeader
    deleted: int
    prev_kvs: typing.List[KeyValue]

    @classmethod
    def from_protobuf(
        cls, pb_value, request: DeleteRangeRequest
    ) -> DeleteRangeResponse:
        return DeleteRangeResponse(
            header=ResponseHeader.from_protobuf(pb_value.header),
            deleted=pb_value.deleted,
            prev_kvs=[KeyValue.from_protobuf(k) for k in pb_value.prev_kvs],
        )


@dataclass
class DeleteRangeRequest(TxnOperation):
    key: bytes
    range_end: bytes
    prev_kv: bool
    _kv: typing.Optional[rpc_pb2_grpc.KVStub] = field(
        hash=False, compare=False, repr=False, default=None
    )
    _response_cls: typing.ClassVar = DeleteRangeResponse

    def as_protobuf(self) -> rpc_pb2.PutRequest:
        return rpc_pb2.DeleteRangeRequest(
            key=self.key,
            range_end=self.range_end,
            prev_kv=self.prev_kv,
        )

    def as_txn_operation(self) -> rpc_pb2.RequestOp:
        return rpc_pb2.RequestOp(request_delete_range=self.as_protobuf())

    def __await__(self) -> DeleteRangeResponse:
        if self._kv is None:
            raise TypeError("RangeRequest is not awaitable")
        response = self._kv.DeleteRange(self.as_protobuf()).__await__()
        return DeleteRangeResponse.from_protobuf(response, self)


@dataclass
class TxnResponse(EtcdResponse):
    header: ResponseHeader
    succeeded: bool
    responses: typing.Sequence["ResponseOp"]

    _key_name: typing.ClassVar = "response_txn"

    @classmethod
    def from_protobuf(cls, pb_value, request: TxnRequest):
        succeeded = pb_value.succeeded
        if succeeded:
            responses = [
                ResponseOp.from_protobuf(r, request.success[i])
                for i, r in enumerate(pb_value.responses)
            ]
        else:
            responses = [
                # request.failure[i]._response_cls.from_response_op(r)
                # for i, r in enumerate(pb_value.responses)
                ResponseOp.from_protobuf(r, request.failure[i])
                for i, r in enumerate(pb_value.responses)
            ]

        return TxnResponse(
            header=ResponseHeader.from_protobuf(pb_value.header),
            succeeded=succeeded,
            responses=responses,
        )


@dataclass
class TxnRequest(TxnOperation):
    compare: typing.Sequence[Compare]
    success: typing.Sequence[TxnOperation]
    failure: typing.Sequence[TxnOperation]
    _kv: typing.Optional[rpc_pb2_grpc.KVStub] = field(
        hash=False, compare=False, repr=False, default=None
    )
    _response_cls: typing.ClassVar = TxnResponse

    def as_protobuf(self):
        return rpc_pb2.TxnRequest(
            compare=[c.as_protobuf() for c in self.compare],
            success=[r.as_txn_operation() for r in self.success],
            failure=[r.as_txn_operation() for r in self.failure],
        )

    def as_txn_operation(self) -> rpc_pb2.RequestOp:
        return rpc_pb2.RequestOp(request_txn=self.as_protobuf())

    def __await__(self) -> TxnResponse:
        if self._kv is None:
            raise TypeError("RangeRequest is not awaitable")
        response = yield from self._kv.Txn(self.as_protobuf()).__await__()
        return TxnResponse.from_protobuf(response, self)


@dataclass
class ResponseOp:
    response: typing.Union[
        RangeResponse, PutResponse, DeleteRangeResponse, TxnResponse
    ]
    response_range: typing.Optional[RangeResponse] = None
    response_put: typing.Optional[PutResponse] = None
    response_delete_range: typing.Optional[DeleteRangeResponse] = None
    response_txn: typing.Optional[TxnResponse] = None

    @classmethod
    def from_protobuf(cls, pb_value, request: TxnOperation) -> ResponseOp:
        response_range = None
        response_put = None
        response_delete_range = None
        response_txn = None
        response: typing.Union[RangeResponse, PutResponse, DeleteRangeResponse, TxnResponse, None] = None
        request_type = type(request)
        if request_type == RangeRequest:
            if typing.TYPE_CHECKING:
                request = typing.cast(RangeRequest, request)
            response = response_range = RangeResponse.from_protobuf(
                pb_value.response_range, request
            )
        elif request_type == PutRequest:
            if typing.TYPE_CHECKING:
                request = typing.cast(PutRequest, request)
            response = response_put = PutResponse.from_protobuf(
                pb_value.response_put, request
            )
        elif request_type == DeleteRangeRequest:
            if typing.TYPE_CHECKING:
                request = typing.cast(DeleteRangeRequest, request)
            response = (
                response_delete_range
            ) = DeleteRangeResponse.from_protobuf(
                pb_value.response_delete_range, request
            )
        elif request_type == TxnRequest:
            if typing.TYPE_CHECKING:
                request = typing.cast(TxnRequest, request)
            response = response_txn = TxnResponse.from_protobuf(
                pb_value.response_txn, request
            )
        if response is None:
            raise RuntimeError(f"Unexpected request type: {request_type}")
        return ResponseOp(
            response=response,
            response_range=response_range,
            response_put=response_put,
            response_delete_range=response_delete_range,
            response_txn=response_txn,
        )


class KVApi:
    def __init__(self, client: Client):
        self._client = client
        self._kv_stub = rpc_pb2_grpc.KVStub(channel=client.channel)

    def range(
        self,
        key: bytes,
        range_end: typing.Optional[bytes] = None,
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
            key,
            range_end,
            limit,
            revision,
            sort_order,
            sort_target,
            serializable,
            keys_only,
            count_only,
            min_mod_revision,
            max_mod_revision,
            min_create_revision,
            max_create_revision,
            _kv=self._kv_stub,
        )

    def put(
        self,
        key: bytes,
        value: bytes,
        lease: int = 0,
        prev_kv: bool = False,
        ignore_value: bool = False,
        ignore_lease: bool = False,
        *,
        timeout: float = 0,
    ) -> PutRequest:
        return PutRequest(
            key,
            value,
            lease,
            prev_kv,
            ignore_value,
            ignore_lease,
            _kv=self._kv_stub,
        )

    def delete_range(
        self,
        key: bytes,
        range_end: bytes,
        prev_kv: bool,
        *,
        timeout: typing.Optional[int] = 0,
    ) -> DeleteRangeRequest:
        return DeleteRangeRequest(key, range_end, prev_kv, self._kv_stub)

    def txn(
        self,
        compare: typing.Sequence[Compare],
        success: typing.Sequence[TxnOperation],
        failure: typing.Sequence[TxnOperation],
        *,
        timeout: typing.Optional[int] = 0,
    ) -> TxnRequest:
        return TxnRequest(compare, success, failure, self._kv_stub)

    async def compact(self, revision: int, physical: bool) -> ResponseHeader:
        ...

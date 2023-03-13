from __future__ import annotations

from grpc.aio._channel import Channel  # type: ignore
from typing_extensions import Protocol

from aioetcd._rpc import rpc_pb2


class KVStub(Protocol):
    def __init__(self, channel: Channel):
        ...

    async def Range(self, request: rpc_pb2.RangeRequest) -> rpc_pb2.RangeResponse:
        ...

    async def Put(self, request: rpc_pb2.PutRequest) -> rpc_pb2.PutResponse:
        ...

    async def DeleteRange(
        self, request: rpc_pb2.DeleteRangeRequest
    ) -> rpc_pb2.DeleteRangeResponse:
        ...

    async def Txn(self, request: rpc_pb2.TxnRequest) -> rpc_pb2.TxnResponse:
        ...

    async def Compact(
        self, request: rpc_pb2.CompactionRequest
    ) -> rpc_pb2.CompactionResponse:
        ...

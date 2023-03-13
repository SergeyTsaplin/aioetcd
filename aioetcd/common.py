from __future__ import annotations

from dataclasses import dataclass

from aioetcd._rpc import rpc_pb2


@dataclass
class ResponseHeader:
    cluster_id: int
    member_id: int
    revision: int
    raft_term: int

    @classmethod
    def from_protobuf(cls, pb_header: rpc_pb2.ResponseHeader) -> ResponseHeader:
        return ResponseHeader(
            cluster_id=pb_header.cluster_id,
            member_id=pb_header.member_id,
            revision=pb_header.revision,
            raft_term=pb_header.raft_term,
        )

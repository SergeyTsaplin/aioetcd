from __future__ import annotations
from dataclasses import dataclass

from aioetcd._rpc_stubs.common import ResponseHeader as ResponseHeaderProto


@dataclass
class ResponseHeader:
    cluster_id: int
    member_id: int
    revision: int
    raft_term: int

    @classmethod
    def from_protobuf(cls, pb_header: ResponseHeaderProto) -> ResponseHeader:
        return ResponseHeader(
            cluster_id=pb_header.cluster_id,
            member_id=pb_header.member_id,
            revision=pb_header.revision,
            raft_term=pb_header.raft_term,
        )

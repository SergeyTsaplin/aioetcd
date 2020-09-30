from dataclasses import dataclass


@dataclass
class ResponseHeader:
    cluster_id: int
    member_id: int
    revision: int
    raft_term: int

    @classmethod
    def from_protobuf(cls, pb_header):
        return ResponseHeader(
            cluster_id=pb_header.cluster_id,
            member_id=pb_header.member_id,
            revision=pb_header.revision,
            raft_term=pb_header.raft_term,
        )

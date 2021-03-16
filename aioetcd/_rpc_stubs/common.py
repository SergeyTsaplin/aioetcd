from typing_extensions import Protocol


class ResponseHeader(Protocol):
    cluster_id: int
    member_id: int
    revision: int
    raft_term: int

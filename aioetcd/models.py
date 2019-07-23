import typing


class EtcdHeaders:
    def __init__(
        self,
        etcd_index: int,
        raft_index: typing.Optional[int],
        raft_terms: typing.Optional[int],
        etcd_cluster_id: typing.Optional[str],
    ):
        self.etcd_index = etcd_index
        self.raft_index = raft_index
        self.raft_terms = raft_terms
        self.etcd_cluster_id = etcd_cluster_id

    @classmethod
    def from_dict(cls, data: typing.Dict[str, str]):
        raw_etcd_index = data["X-Etcd-Index"]
        raw_raft_index = data.get("X-Raft-Index")
        raw_raft_terms = data.get("X-Raft-Term")
        etcd_cluster_id = data.get("X-Etcd-Cluster-Id")
        etcd_index = int(raw_etcd_index)
        raft_index = int(raw_raft_index) if raw_raft_index else None
        raft_terms = int(raw_raft_terms) if raw_raft_terms else None
        return cls(etcd_index, raft_index, raft_terms, etcd_cluster_id)

    def __repr__(self):
        return (
            "EtcdHeaders("
            "etcd_index={0.etcd_index}, "
            "raft_index={0.raft_index}, "
            "raft_terms={0.raft_terms}, "
            "etcd_cluster_id={0.etcd_cluster_id}"
            ")".format(self)
        )


class VersionResponse:
    def __init__(self, server, cluster):
        self.etcdserver = server  # type: str
        self.etcdcluster = cluster  # type: str

    @classmethod
    def from_dict(cls, data):
        return cls(data["etcdserver"], data["etcdcluster"])


class Node:
    @classmethod
    def from_dict(cls, data: typing.Dict) -> "Node":
        raise NotImplementedError()


class GetNode(Node):
    def __init__(
        self,
        created_index: int,
        key: str,
        modified_index: int,
        value: typing.Optional[str],
    ):
        self.created_index = created_index
        self.key = key
        self.modified_index = modified_index
        self.value = value

    @classmethod
    def from_dict(cls, data: typing.Dict) -> "GetNode":
        created_index = data["createdIndex"]
        key = data["key"]
        modified_index = data["modifiedIndex"]
        value = data["value"]
        return cls(created_index, key, modified_index, value)

    def __repr__(self):
        return (
            'Node(created_index={ci}, key="{key}", modified_index={mi}, '
            'value="{value}")'.format(
                ci=self.created_index,
                key=self.key,
                mi=self.modified_index,
                value=self.value,
            )
        )


class ErrorResponse:
    def __init__(self, error_code, message, cause, index):
        self.error_code = error_code  # type: int
        self.message = message  # type: str
        self.cause = cause  # type: str
        self.index = index  # type: int

    @classmethod
    def from_dict(cls, data) -> "ErrorResponse":
        return cls(
            data["errorCode"], data["message"], data["cause"], data["index"]
        )

    def __repr__(self):
        return (
            "ErrorResponse(error_code={code}, message={message}, "
            "cause={cause}, index={index}".format(
                code=self.error_code,
                message=self.message,
                cause=self.cause,
                index=self.index,
            )
        )


class EtcdResponse:
    _NODE_CLS = Node  # type: typing.ClassVar[typing.Type[Node]]

    def __init__(
        self,
        action: str,
        node: Node,
        prev_node: typing.Optional[Node] = None,
        headers: typing.Optional[EtcdHeaders] = None,
    ):
        self.action = action
        self.node = node
        self.prev_node = prev_node
        self.headers = headers

    def set_headers(self, headers: typing.Dict[str, str]):
        self.headers = EtcdHeaders.from_dict(headers)

    @classmethod
    def from_dict(cls, data: typing.Dict):
        action = data["action"]
        node = cls._NODE_CLS.from_dict(data["node"])
        raw_prev_node = data.get("prevNode")
        prev_node = None
        if raw_prev_node:
            prev_node = cls._NODE_CLS.from_dict(raw_prev_node)
        return cls(action, node, prev_node)

    def __repr__(self):
        if self.prev_node is None:
            return '{cls_name}(action="{action}", node={node})'.format(
                cls_name=self.__class__.__name__,
                action=self.action,
                node=self.node,
            )
        else:
            return (
                '{cls_name}(action="{action}", node={node}, '
                "prev_node={prev_node})".format(
                    cls_name=self.__class__.__name__,
                    action=self.action,
                    node=self.node,
                    prev_node=self.prev_node,
                )
            )


class GetResponse(EtcdResponse):
    _NODE_CLS = GetNode


class SetResponse(EtcdResponse):
    _NODE_CLS = GetNode

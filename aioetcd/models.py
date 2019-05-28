import typing


JSON_DICT = typing.Dict


class VersionResponse:
    def __init__(self, server, cluster):
        self.etcdserver = server  # type: str
        self.etcdcluster = cluster  # type: str

    @classmethod
    def from_dict(cls, data):
        return cls(data['etcdserver'], data['etcdcluster'])


class Node:
    @classmethod
    def from_dict(cls, data: typing.Dict) -> 'Node':
        raise NotImplementedError()


class GetNode(Node):
    def __init__(
            self,
            created_index: int,
            key: str,
            modified_index: int,
            value: str
    ):
        self.created_index = created_index
        self.key = key
        self.modified_index = modified_index
        self.value = value

    @classmethod
    def from_dict(cls, data: typing.Dict) -> 'GetNode':
        created_index = data['createdIndex']
        key = data['key']
        modified_index = data['modifiedIndex']
        value = data['value']
        return cls(created_index, key, modified_index, value)

    def __repr__(self):
        return 'Node(created_index={ci}, key="{key}", modified_index={mi}, ' \
            'value="{value}")'.format(
                ci=self.created_index,
                key=self.key,
                mi=self.modified_index,
                value=self.value
            )


class ErrorResponse:
    def __init__(self, error_code, message, cause, index):
        self.error_code = error_code  # type: int
        self.message = message  # type: str
        self.cause = cause  # type: str
        self.index = index  # type: int

    @classmethod
    def from_dict(cls, data) -> 'ErrorResponse':
        return cls(
            data['errorCode'], data['message'], data['cause'], data['index']
        )

    def __repr__(self):
        return 'ErrorResponse(error_code={code}, message={message}, '\
            'cause={cause}, index={index}'.format(
                code=self.error_code,
                message=self.message,
                cause=self.cause,
                index=self.index
            )


class EtcdResponse:
    _NODE_CLS = Node  # type: typing.ClassVar[typing.Type[Node]]

    def __init__(self, action: str, node: Node):
        self.action = action
        self.node = node

    @classmethod
    def from_dict(cls, data: typing.Dict):
        action = data['action']
        node = cls._NODE_CLS.from_dict(data['node'])
        return cls(action, node)

    def __repr__(self):
        return '{cls_name}(action="{action}", node={node})'.format(
            cls_name=self.__class__.__name__,
            action=self.action,
            node=self.node
        )


class GetResponse(EtcdResponse):
    _NODE_CLS = GetNode

    def __init__(self, action: str, node: GetNode):
        self.action = action  # type: str
        self.node = node  # type GetNode

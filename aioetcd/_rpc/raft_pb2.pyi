"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

global___EntryType = EntryType
class _EntryType(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[EntryType.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    EntryNormal = EntryType.V(0)
    EntryConfChange = EntryType.V(1)
    EntryConfChangeV2 = EntryType.V(2)
class EntryType(metaclass=_EntryType):
    V = typing.NewType('V', builtins.int)
EntryNormal = EntryType.V(0)
EntryConfChange = EntryType.V(1)
EntryConfChangeV2 = EntryType.V(2)

global___MessageType = MessageType
class _MessageType(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[MessageType.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    MsgHup = MessageType.V(0)
    MsgBeat = MessageType.V(1)
    MsgProp = MessageType.V(2)
    MsgApp = MessageType.V(3)
    MsgAppResp = MessageType.V(4)
    MsgVote = MessageType.V(5)
    MsgVoteResp = MessageType.V(6)
    MsgSnap = MessageType.V(7)
    MsgHeartbeat = MessageType.V(8)
    MsgHeartbeatResp = MessageType.V(9)
    MsgUnreachable = MessageType.V(10)
    MsgSnapStatus = MessageType.V(11)
    MsgCheckQuorum = MessageType.V(12)
    MsgTransferLeader = MessageType.V(13)
    MsgTimeoutNow = MessageType.V(14)
    MsgReadIndex = MessageType.V(15)
    MsgReadIndexResp = MessageType.V(16)
    MsgPreVote = MessageType.V(17)
    MsgPreVoteResp = MessageType.V(18)
class MessageType(metaclass=_MessageType):
    V = typing.NewType('V', builtins.int)
MsgHup = MessageType.V(0)
MsgBeat = MessageType.V(1)
MsgProp = MessageType.V(2)
MsgApp = MessageType.V(3)
MsgAppResp = MessageType.V(4)
MsgVote = MessageType.V(5)
MsgVoteResp = MessageType.V(6)
MsgSnap = MessageType.V(7)
MsgHeartbeat = MessageType.V(8)
MsgHeartbeatResp = MessageType.V(9)
MsgUnreachable = MessageType.V(10)
MsgSnapStatus = MessageType.V(11)
MsgCheckQuorum = MessageType.V(12)
MsgTransferLeader = MessageType.V(13)
MsgTimeoutNow = MessageType.V(14)
MsgReadIndex = MessageType.V(15)
MsgReadIndexResp = MessageType.V(16)
MsgPreVote = MessageType.V(17)
MsgPreVoteResp = MessageType.V(18)

global___ConfChangeTransition = ConfChangeTransition
class _ConfChangeTransition(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ConfChangeTransition.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    ConfChangeTransitionAuto = ConfChangeTransition.V(0)
    ConfChangeTransitionJointImplicit = ConfChangeTransition.V(1)
    ConfChangeTransitionJointExplicit = ConfChangeTransition.V(2)
class ConfChangeTransition(metaclass=_ConfChangeTransition):
    V = typing.NewType('V', builtins.int)
ConfChangeTransitionAuto = ConfChangeTransition.V(0)
ConfChangeTransitionJointImplicit = ConfChangeTransition.V(1)
ConfChangeTransitionJointExplicit = ConfChangeTransition.V(2)

global___ConfChangeType = ConfChangeType
class _ConfChangeType(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ConfChangeType.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    ConfChangeAddNode = ConfChangeType.V(0)
    ConfChangeRemoveNode = ConfChangeType.V(1)
    ConfChangeUpdateNode = ConfChangeType.V(2)
    ConfChangeAddLearnerNode = ConfChangeType.V(3)
class ConfChangeType(metaclass=_ConfChangeType):
    V = typing.NewType('V', builtins.int)
ConfChangeAddNode = ConfChangeType.V(0)
ConfChangeRemoveNode = ConfChangeType.V(1)
ConfChangeUpdateNode = ConfChangeType.V(2)
ConfChangeAddLearnerNode = ConfChangeType.V(3)

class Entry(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TERM_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    Term: builtins.int = ...
    Index: builtins.int = ...
    Type: global___EntryType.V = ...
    Data: builtins.bytes = ...

    def __init__(self,
        *,
        Term : typing.Optional[builtins.int] = ...,
        Index : typing.Optional[builtins.int] = ...,
        Type : typing.Optional[global___EntryType.V] = ...,
        Data : typing.Optional[builtins.bytes] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"Data",b"Data",u"Index",b"Index",u"Term",b"Term",u"Type",b"Type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"Data",b"Data",u"Index",b"Index",u"Term",b"Term",u"Type",b"Type"]) -> None: ...
global___Entry = Entry

class SnapshotMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONF_STATE_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    TERM_FIELD_NUMBER: builtins.int
    index: builtins.int = ...
    term: builtins.int = ...

    @property
    def conf_state(self) -> global___ConfState: ...

    def __init__(self,
        *,
        conf_state : typing.Optional[global___ConfState] = ...,
        index : typing.Optional[builtins.int] = ...,
        term : typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"conf_state",b"conf_state",u"index",b"index",u"term",b"term"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"conf_state",b"conf_state",u"index",b"index",u"term",b"term"]) -> None: ...
global___SnapshotMetadata = SnapshotMetadata

class Snapshot(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATA_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    data: builtins.bytes = ...

    @property
    def metadata(self) -> global___SnapshotMetadata: ...

    def __init__(self,
        *,
        data : typing.Optional[builtins.bytes] = ...,
        metadata : typing.Optional[global___SnapshotMetadata] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"data",b"data",u"metadata",b"metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"data",b"data",u"metadata",b"metadata"]) -> None: ...
global___Snapshot = Snapshot

class Message(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TYPE_FIELD_NUMBER: builtins.int
    TO_FIELD_NUMBER: builtins.int
    FROM_FIELD_NUMBER: builtins.int
    TERM_FIELD_NUMBER: builtins.int
    LOGTERM_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    ENTRIES_FIELD_NUMBER: builtins.int
    COMMIT_FIELD_NUMBER: builtins.int
    SNAPSHOT_FIELD_NUMBER: builtins.int
    REJECT_FIELD_NUMBER: builtins.int
    REJECTHINT_FIELD_NUMBER: builtins.int
    CONTEXT_FIELD_NUMBER: builtins.int
    type: global___MessageType.V = ...
    to: builtins.int = ...
    term: builtins.int = ...
    logTerm: builtins.int = ...
    index: builtins.int = ...
    commit: builtins.int = ...
    reject: builtins.bool = ...
    rejectHint: builtins.int = ...
    context: builtins.bytes = ...

    @property
    def entries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Entry]: ...

    @property
    def snapshot(self) -> global___Snapshot: ...

    def __init__(self,
        *,
        type : typing.Optional[global___MessageType.V] = ...,
        to : typing.Optional[builtins.int] = ...,
        term : typing.Optional[builtins.int] = ...,
        logTerm : typing.Optional[builtins.int] = ...,
        index : typing.Optional[builtins.int] = ...,
        entries : typing.Optional[typing.Iterable[global___Entry]] = ...,
        commit : typing.Optional[builtins.int] = ...,
        snapshot : typing.Optional[global___Snapshot] = ...,
        reject : typing.Optional[builtins.bool] = ...,
        rejectHint : typing.Optional[builtins.int] = ...,
        context : typing.Optional[builtins.bytes] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"commit",b"commit",u"context",b"context",u"from",b"from",u"index",b"index",u"logTerm",b"logTerm",u"reject",b"reject",u"rejectHint",b"rejectHint",u"snapshot",b"snapshot",u"term",b"term",u"to",b"to",u"type",b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"commit",b"commit",u"context",b"context",u"entries",b"entries",u"from",b"from",u"index",b"index",u"logTerm",b"logTerm",u"reject",b"reject",u"rejectHint",b"rejectHint",u"snapshot",b"snapshot",u"term",b"term",u"to",b"to",u"type",b"type"]) -> None: ...
global___Message = Message

class HardState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TERM_FIELD_NUMBER: builtins.int
    VOTE_FIELD_NUMBER: builtins.int
    COMMIT_FIELD_NUMBER: builtins.int
    term: builtins.int = ...
    vote: builtins.int = ...
    commit: builtins.int = ...

    def __init__(self,
        *,
        term : typing.Optional[builtins.int] = ...,
        vote : typing.Optional[builtins.int] = ...,
        commit : typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"commit",b"commit",u"term",b"term",u"vote",b"vote"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"commit",b"commit",u"term",b"term",u"vote",b"vote"]) -> None: ...
global___HardState = HardState

class ConfState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VOTERS_FIELD_NUMBER: builtins.int
    LEARNERS_FIELD_NUMBER: builtins.int
    VOTERS_OUTGOING_FIELD_NUMBER: builtins.int
    LEARNERS_NEXT_FIELD_NUMBER: builtins.int
    AUTO_LEAVE_FIELD_NUMBER: builtins.int
    voters: google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int] = ...
    learners: google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int] = ...
    voters_outgoing: google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int] = ...
    learners_next: google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int] = ...
    auto_leave: builtins.bool = ...

    def __init__(self,
        *,
        voters : typing.Optional[typing.Iterable[builtins.int]] = ...,
        learners : typing.Optional[typing.Iterable[builtins.int]] = ...,
        voters_outgoing : typing.Optional[typing.Iterable[builtins.int]] = ...,
        learners_next : typing.Optional[typing.Iterable[builtins.int]] = ...,
        auto_leave : typing.Optional[builtins.bool] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"auto_leave",b"auto_leave"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"auto_leave",b"auto_leave",u"learners",b"learners",u"learners_next",b"learners_next",u"voters",b"voters",u"voters_outgoing",b"voters_outgoing"]) -> None: ...
global___ConfState = ConfState

class ConfChange(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TYPE_FIELD_NUMBER: builtins.int
    NODE_ID_FIELD_NUMBER: builtins.int
    CONTEXT_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    type: global___ConfChangeType.V = ...
    node_id: builtins.int = ...
    context: builtins.bytes = ...
    id: builtins.int = ...

    def __init__(self,
        *,
        type : typing.Optional[global___ConfChangeType.V] = ...,
        node_id : typing.Optional[builtins.int] = ...,
        context : typing.Optional[builtins.bytes] = ...,
        id : typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"context",b"context",u"id",b"id",u"node_id",b"node_id",u"type",b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"context",b"context",u"id",b"id",u"node_id",b"node_id",u"type",b"type"]) -> None: ...
global___ConfChange = ConfChange

class ConfChangeSingle(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TYPE_FIELD_NUMBER: builtins.int
    NODE_ID_FIELD_NUMBER: builtins.int
    type: global___ConfChangeType.V = ...
    node_id: builtins.int = ...

    def __init__(self,
        *,
        type : typing.Optional[global___ConfChangeType.V] = ...,
        node_id : typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"node_id",b"node_id",u"type",b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"node_id",b"node_id",u"type",b"type"]) -> None: ...
global___ConfChangeSingle = ConfChangeSingle

class ConfChangeV2(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TRANSITION_FIELD_NUMBER: builtins.int
    CHANGES_FIELD_NUMBER: builtins.int
    CONTEXT_FIELD_NUMBER: builtins.int
    transition: global___ConfChangeTransition.V = ...
    context: builtins.bytes = ...

    @property
    def changes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ConfChangeSingle]: ...

    def __init__(self,
        *,
        transition : typing.Optional[global___ConfChangeTransition.V] = ...,
        changes : typing.Optional[typing.Iterable[global___ConfChangeSingle]] = ...,
        context : typing.Optional[builtins.bytes] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"context",b"context",u"transition",b"transition"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"changes",b"changes",u"context",b"context",u"transition",b"transition"]) -> None: ...
global___ConfChangeV2 = ConfChangeV2
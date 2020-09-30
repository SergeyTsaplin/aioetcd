# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v3election.proto

import sys

_b = (
    sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
)
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import rpc_pb2 as rpc__pb2
from . import kv_pb2 as kv__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="v3election.proto",
    package="v3electionpb",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=_b(
        '\n\x10v3election.proto\x12\x0cv3electionpb\x1a\trpc.proto\x1a\x08kv.proto"=\n\x0f\x43\x61mpaignRequest\x12\x0c\n\x04name\x18\x01 \x01(\x0c\x12\r\n\x05lease\x18\x02 \x01(\x03\x12\r\n\x05value\x18\x03 \x01(\x0c"i\n\x10\x43\x61mpaignResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12\'\n\x06leader\x18\x02 \x01(\x0b\x32\x17.v3electionpb.LeaderKey"B\n\tLeaderKey\x12\x0c\n\x04name\x18\x01 \x01(\x0c\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\x0b\n\x03rev\x18\x03 \x01(\x03\x12\r\n\x05lease\x18\x04 \x01(\x03"\x1d\n\rLeaderRequest\x12\x0c\n\x04name\x18\x01 \x01(\x0c"\\\n\x0eLeaderResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12\x1c\n\x02kv\x18\x02 \x01(\x0b\x32\x10.mvccpb.KeyValue"8\n\rResignRequest\x12\'\n\x06leader\x18\x01 \x01(\x0b\x32\x17.v3electionpb.LeaderKey">\n\x0eResignResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader"I\n\x0fProclaimRequest\x12\'\n\x06leader\x18\x01 \x01(\x0b\x32\x17.v3electionpb.LeaderKey\x12\r\n\x05value\x18\x02 \x01(\x0c"@\n\x10ProclaimResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader2\xfc\x02\n\x08\x45lection\x12K\n\x08\x43\x61mpaign\x12\x1d.v3electionpb.CampaignRequest\x1a\x1e.v3electionpb.CampaignResponse"\x00\x12K\n\x08Proclaim\x12\x1d.v3electionpb.ProclaimRequest\x1a\x1e.v3electionpb.ProclaimResponse"\x00\x12\x45\n\x06Leader\x12\x1b.v3electionpb.LeaderRequest\x1a\x1c.v3electionpb.LeaderResponse"\x00\x12H\n\x07Observe\x12\x1b.v3electionpb.LeaderRequest\x1a\x1c.v3electionpb.LeaderResponse"\x00\x30\x01\x12\x45\n\x06Resign\x12\x1b.v3electionpb.ResignRequest\x1a\x1c.v3electionpb.ResignResponse"\x00\x62\x06proto3'
    ),
    dependencies=[rpc__pb2.DESCRIPTOR, kv__pb2.DESCRIPTOR,],
)


_CAMPAIGNREQUEST = _descriptor.Descriptor(
    name="CampaignRequest",
    full_name="v3electionpb.CampaignRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="v3electionpb.CampaignRequest.name",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="lease",
            full_name="v3electionpb.CampaignRequest.lease",
            index=1,
            number=2,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="v3electionpb.CampaignRequest.value",
            index=2,
            number=3,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=55,
    serialized_end=116,
)


_CAMPAIGNRESPONSE = _descriptor.Descriptor(
    name="CampaignResponse",
    full_name="v3electionpb.CampaignResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="v3electionpb.CampaignResponse.header",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="leader",
            full_name="v3electionpb.CampaignResponse.leader",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=118,
    serialized_end=223,
)


_LEADERKEY = _descriptor.Descriptor(
    name="LeaderKey",
    full_name="v3electionpb.LeaderKey",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="v3electionpb.LeaderKey.name",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="key",
            full_name="v3electionpb.LeaderKey.key",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="rev",
            full_name="v3electionpb.LeaderKey.rev",
            index=2,
            number=3,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="lease",
            full_name="v3electionpb.LeaderKey.lease",
            index=3,
            number=4,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=225,
    serialized_end=291,
)


_LEADERREQUEST = _descriptor.Descriptor(
    name="LeaderRequest",
    full_name="v3electionpb.LeaderRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="v3electionpb.LeaderRequest.name",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=293,
    serialized_end=322,
)


_LEADERRESPONSE = _descriptor.Descriptor(
    name="LeaderResponse",
    full_name="v3electionpb.LeaderResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="v3electionpb.LeaderResponse.header",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="kv",
            full_name="v3electionpb.LeaderResponse.kv",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=324,
    serialized_end=416,
)


_RESIGNREQUEST = _descriptor.Descriptor(
    name="ResignRequest",
    full_name="v3electionpb.ResignRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="leader",
            full_name="v3electionpb.ResignRequest.leader",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=418,
    serialized_end=474,
)


_RESIGNRESPONSE = _descriptor.Descriptor(
    name="ResignResponse",
    full_name="v3electionpb.ResignResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="v3electionpb.ResignResponse.header",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=476,
    serialized_end=538,
)


_PROCLAIMREQUEST = _descriptor.Descriptor(
    name="ProclaimRequest",
    full_name="v3electionpb.ProclaimRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="leader",
            full_name="v3electionpb.ProclaimRequest.leader",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="v3electionpb.ProclaimRequest.value",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=540,
    serialized_end=613,
)


_PROCLAIMRESPONSE = _descriptor.Descriptor(
    name="ProclaimResponse",
    full_name="v3electionpb.ProclaimResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="v3electionpb.ProclaimResponse.header",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=615,
    serialized_end=679,
)

_CAMPAIGNRESPONSE.fields_by_name[
    "header"
].message_type = rpc__pb2._RESPONSEHEADER
_CAMPAIGNRESPONSE.fields_by_name["leader"].message_type = _LEADERKEY
_LEADERRESPONSE.fields_by_name[
    "header"
].message_type = rpc__pb2._RESPONSEHEADER
_LEADERRESPONSE.fields_by_name["kv"].message_type = kv__pb2._KEYVALUE
_RESIGNREQUEST.fields_by_name["leader"].message_type = _LEADERKEY
_RESIGNRESPONSE.fields_by_name[
    "header"
].message_type = rpc__pb2._RESPONSEHEADER
_PROCLAIMREQUEST.fields_by_name["leader"].message_type = _LEADERKEY
_PROCLAIMRESPONSE.fields_by_name[
    "header"
].message_type = rpc__pb2._RESPONSEHEADER
DESCRIPTOR.message_types_by_name["CampaignRequest"] = _CAMPAIGNREQUEST
DESCRIPTOR.message_types_by_name["CampaignResponse"] = _CAMPAIGNRESPONSE
DESCRIPTOR.message_types_by_name["LeaderKey"] = _LEADERKEY
DESCRIPTOR.message_types_by_name["LeaderRequest"] = _LEADERREQUEST
DESCRIPTOR.message_types_by_name["LeaderResponse"] = _LEADERRESPONSE
DESCRIPTOR.message_types_by_name["ResignRequest"] = _RESIGNREQUEST
DESCRIPTOR.message_types_by_name["ResignResponse"] = _RESIGNRESPONSE
DESCRIPTOR.message_types_by_name["ProclaimRequest"] = _PROCLAIMREQUEST
DESCRIPTOR.message_types_by_name["ProclaimResponse"] = _PROCLAIMRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignRequest = _reflection.GeneratedProtocolMessageType(
    "CampaignRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CAMPAIGNREQUEST,
        "__module__": "v3election_pb2"
        # @@protoc_insertion_point(class_scope:v3electionpb.CampaignRequest)
    },
)
_sym_db.RegisterMessage(CampaignRequest)

CampaignResponse = _reflection.GeneratedProtocolMessageType(
    "CampaignResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CAMPAIGNRESPONSE,
        "__module__": "v3election_pb2"
        # @@protoc_insertion_point(class_scope:v3electionpb.CampaignResponse)
    },
)
_sym_db.RegisterMessage(CampaignResponse)

LeaderKey = _reflection.GeneratedProtocolMessageType(
    "LeaderKey",
    (_message.Message,),
    {
        "DESCRIPTOR": _LEADERKEY,
        "__module__": "v3election_pb2"
        # @@protoc_insertion_point(class_scope:v3electionpb.LeaderKey)
    },
)
_sym_db.RegisterMessage(LeaderKey)

LeaderRequest = _reflection.GeneratedProtocolMessageType(
    "LeaderRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LEADERREQUEST,
        "__module__": "v3election_pb2"
        # @@protoc_insertion_point(class_scope:v3electionpb.LeaderRequest)
    },
)
_sym_db.RegisterMessage(LeaderRequest)

LeaderResponse = _reflection.GeneratedProtocolMessageType(
    "LeaderResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _LEADERRESPONSE,
        "__module__": "v3election_pb2"
        # @@protoc_insertion_point(class_scope:v3electionpb.LeaderResponse)
    },
)
_sym_db.RegisterMessage(LeaderResponse)

ResignRequest = _reflection.GeneratedProtocolMessageType(
    "ResignRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESIGNREQUEST,
        "__module__": "v3election_pb2"
        # @@protoc_insertion_point(class_scope:v3electionpb.ResignRequest)
    },
)
_sym_db.RegisterMessage(ResignRequest)

ResignResponse = _reflection.GeneratedProtocolMessageType(
    "ResignResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESIGNRESPONSE,
        "__module__": "v3election_pb2"
        # @@protoc_insertion_point(class_scope:v3electionpb.ResignResponse)
    },
)
_sym_db.RegisterMessage(ResignResponse)

ProclaimRequest = _reflection.GeneratedProtocolMessageType(
    "ProclaimRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _PROCLAIMREQUEST,
        "__module__": "v3election_pb2"
        # @@protoc_insertion_point(class_scope:v3electionpb.ProclaimRequest)
    },
)
_sym_db.RegisterMessage(ProclaimRequest)

ProclaimResponse = _reflection.GeneratedProtocolMessageType(
    "ProclaimResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _PROCLAIMRESPONSE,
        "__module__": "v3election_pb2"
        # @@protoc_insertion_point(class_scope:v3electionpb.ProclaimResponse)
    },
)
_sym_db.RegisterMessage(ProclaimResponse)


_ELECTION = _descriptor.ServiceDescriptor(
    name="Election",
    full_name="v3electionpb.Election",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=682,
    serialized_end=1062,
    methods=[
        _descriptor.MethodDescriptor(
            name="Campaign",
            full_name="v3electionpb.Election.Campaign",
            index=0,
            containing_service=None,
            input_type=_CAMPAIGNREQUEST,
            output_type=_CAMPAIGNRESPONSE,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name="Proclaim",
            full_name="v3electionpb.Election.Proclaim",
            index=1,
            containing_service=None,
            input_type=_PROCLAIMREQUEST,
            output_type=_PROCLAIMRESPONSE,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name="Leader",
            full_name="v3electionpb.Election.Leader",
            index=2,
            containing_service=None,
            input_type=_LEADERREQUEST,
            output_type=_LEADERRESPONSE,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name="Observe",
            full_name="v3electionpb.Election.Observe",
            index=3,
            containing_service=None,
            input_type=_LEADERREQUEST,
            output_type=_LEADERRESPONSE,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name="Resign",
            full_name="v3electionpb.Election.Resign",
            index=4,
            containing_service=None,
            input_type=_RESIGNREQUEST,
            output_type=_RESIGNRESPONSE,
            serialized_options=None,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_ELECTION)

DESCRIPTOR.services_by_name["Election"] = _ELECTION

# @@protoc_insertion_point(module_scope)

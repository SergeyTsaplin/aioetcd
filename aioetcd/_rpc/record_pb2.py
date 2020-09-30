# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: record.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
    name="record.proto",
    package="walpb",
    syntax="proto2",
    serialized_options=None,
    serialized_pb=_b(
        '\n\x0crecord.proto\x12\x05walpb"1\n\x06Record\x12\x0c\n\x04type\x18\x01 \x01(\x03\x12\x0b\n\x03\x63rc\x18\x02 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c"\'\n\x08Snapshot\x12\r\n\x05index\x18\x01 \x01(\x04\x12\x0c\n\x04term\x18\x02 \x01(\x04'
    ),
)


_RECORD = _descriptor.Descriptor(
    name="Record",
    full_name="walpb.Record",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="walpb.Record.type",
            index=0,
            number=1,
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
            name="crc",
            full_name="walpb.Record.crc",
            index=1,
            number=2,
            type=13,
            cpp_type=3,
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
            name="data",
            full_name="walpb.Record.data",
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
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=23,
    serialized_end=72,
)


_SNAPSHOT = _descriptor.Descriptor(
    name="Snapshot",
    full_name="walpb.Snapshot",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="index",
            full_name="walpb.Snapshot.index",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
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
            name="term",
            full_name="walpb.Snapshot.term",
            index=1,
            number=2,
            type=4,
            cpp_type=4,
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
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=74,
    serialized_end=113,
)

DESCRIPTOR.message_types_by_name["Record"] = _RECORD
DESCRIPTOR.message_types_by_name["Snapshot"] = _SNAPSHOT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Record = _reflection.GeneratedProtocolMessageType(
    "Record",
    (_message.Message,),
    {
        "DESCRIPTOR": _RECORD,
        "__module__": "record_pb2"
        # @@protoc_insertion_point(class_scope:walpb.Record)
    },
)
_sym_db.RegisterMessage(Record)

Snapshot = _reflection.GeneratedProtocolMessageType(
    "Snapshot",
    (_message.Message,),
    {
        "DESCRIPTOR": _SNAPSHOT,
        "__module__": "record_pb2"
        # @@protoc_insertion_point(class_scope:walpb.Snapshot)
    },
)
_sym_db.RegisterMessage(Snapshot)


# @@protoc_insertion_point(module_scope)

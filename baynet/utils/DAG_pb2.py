# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: baynet/utils/DAG.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='baynet/utils/DAG.proto',
  package='baynet',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x16\x62\x61ynet/utils/DAG.proto\x12\x06\x62\x61ynet\"\"\n\x03\x44\x41G\x12\x1b\n\x05nodes\x18\x01 \x03(\x0b\x32\x0c.baynet.Node\"\x80\x01\n\x04Node\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\'\n\rvariable_type\x18\x02 \x01(\x0e\x32\x10.baynet.NodeType\x12\x0e\n\x06levels\x18\x03 \x03(\t\x12\x0f\n\x07parents\x18\x04 \x03(\t\x12 \n\tcpd_array\x18\x05 \x01(\x0b\x32\r.baynet.Array\"*\n\x05\x41rray\x12\r\n\x05shape\x18\x01 \x03(\x05\x12\x12\n\nflat_array\x18\x02 \x01(\x0c*3\n\x08NodeType\x12\x0c\n\x08\x44ISCRETE\x10\x00\x12\x0e\n\nCONTINUOUS\x10\x01\x12\t\n\x05MIXED\x10\x02\x62\x06proto3'
)

_NODETYPE = _descriptor.EnumDescriptor(
  name='NodeType',
  full_name='baynet.NodeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DISCRETE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTINUOUS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIXED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=245,
  serialized_end=296,
)
_sym_db.RegisterEnumDescriptor(_NODETYPE)

NodeType = enum_type_wrapper.EnumTypeWrapper(_NODETYPE)
DISCRETE = 0
CONTINUOUS = 1
MIXED = 2



_DAG = _descriptor.Descriptor(
  name='DAG',
  full_name='baynet.DAG',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='baynet.DAG.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=68,
)


_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='baynet.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='baynet.Node.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variable_type', full_name='baynet.Node.variable_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='levels', full_name='baynet.Node.levels', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parents', full_name='baynet.Node.parents', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpd_array', full_name='baynet.Node.cpd_array', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=199,
)


_ARRAY = _descriptor.Descriptor(
  name='Array',
  full_name='baynet.Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shape', full_name='baynet.Array.shape', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flat_array', full_name='baynet.Array.flat_array', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=201,
  serialized_end=243,
)

_DAG.fields_by_name['nodes'].message_type = _NODE
_NODE.fields_by_name['variable_type'].enum_type = _NODETYPE
_NODE.fields_by_name['cpd_array'].message_type = _ARRAY
DESCRIPTOR.message_types_by_name['DAG'] = _DAG
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['Array'] = _ARRAY
DESCRIPTOR.enum_types_by_name['NodeType'] = _NODETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DAG = _reflection.GeneratedProtocolMessageType('DAG', (_message.Message,), {
  'DESCRIPTOR' : _DAG,
  '__module__' : 'baynet.utils.DAG_pb2'
  # @@protoc_insertion_point(class_scope:baynet.DAG)
  })
_sym_db.RegisterMessage(DAG)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {
  'DESCRIPTOR' : _NODE,
  '__module__' : 'baynet.utils.DAG_pb2'
  # @@protoc_insertion_point(class_scope:baynet.Node)
  })
_sym_db.RegisterMessage(Node)

Array = _reflection.GeneratedProtocolMessageType('Array', (_message.Message,), {
  'DESCRIPTOR' : _ARRAY,
  '__module__' : 'baynet.utils.DAG_pb2'
  # @@protoc_insertion_point(class_scope:baynet.Array)
  })
_sym_db.RegisterMessage(Array)


# @@protoc_insertion_point(module_scope)
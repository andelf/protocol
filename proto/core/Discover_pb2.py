# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core/Discover.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='core/Discover.proto',
  package='protocol',
  syntax='proto3',
  serialized_options=_b('\n\017org.tron.protosB\010DiscoverZ)github.com/tronprotocol/grpc-gateway/core'),
  serialized_pb=_b('\n\x13\x63ore/Discover.proto\x12\x08protocol\"9\n\x08\x45ndpoint\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x0e\n\x06nodeId\x18\x03 \x01(\x0c\"s\n\x0bPingMessage\x12 \n\x04\x66rom\x18\x01 \x01(\x0b\x32\x12.protocol.Endpoint\x12\x1e\n\x02to\x18\x02 \x01(\x0b\x32\x12.protocol.Endpoint\x12\x0f\n\x07version\x18\x03 \x01(\x05\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\"P\n\x0bPongMessage\x12 \n\x04\x66rom\x18\x01 \x01(\x0b\x32\x12.protocol.Endpoint\x12\x0c\n\x04\x65\x63ho\x18\x02 \x01(\x05\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\"W\n\x0e\x46indNeighbours\x12 \n\x04\x66rom\x18\x01 \x01(\x0b\x32\x12.protocol.Endpoint\x12\x10\n\x08targetId\x18\x02 \x01(\x0c\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\"i\n\nNeighbours\x12 \n\x04\x66rom\x18\x01 \x01(\x0b\x32\x12.protocol.Endpoint\x12&\n\nneighbours\x18\x02 \x03(\x0b\x32\x12.protocol.Endpoint\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\"/\n\rBackupMessage\x12\x0c\n\x04\x66lag\x18\x01 \x01(\x08\x12\x10\n\x08priority\x18\x02 \x01(\x05\x42\x46\n\x0forg.tron.protosB\x08\x44iscoverZ)github.com/tronprotocol/grpc-gateway/coreb\x06proto3')
)




_ENDPOINT = _descriptor.Descriptor(
  name='Endpoint',
  full_name='protocol.Endpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='protocol.Endpoint.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='protocol.Endpoint.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodeId', full_name='protocol.Endpoint.nodeId', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=33,
  serialized_end=90,
)


_PINGMESSAGE = _descriptor.Descriptor(
  name='PingMessage',
  full_name='protocol.PingMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='protocol.PingMessage.from', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to', full_name='protocol.PingMessage.to', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='protocol.PingMessage.version', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='protocol.PingMessage.timestamp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=92,
  serialized_end=207,
)


_PONGMESSAGE = _descriptor.Descriptor(
  name='PongMessage',
  full_name='protocol.PongMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='protocol.PongMessage.from', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='echo', full_name='protocol.PongMessage.echo', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='protocol.PongMessage.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=209,
  serialized_end=289,
)


_FINDNEIGHBOURS = _descriptor.Descriptor(
  name='FindNeighbours',
  full_name='protocol.FindNeighbours',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='protocol.FindNeighbours.from', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetId', full_name='protocol.FindNeighbours.targetId', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='protocol.FindNeighbours.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=291,
  serialized_end=378,
)


_NEIGHBOURS = _descriptor.Descriptor(
  name='Neighbours',
  full_name='protocol.Neighbours',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='protocol.Neighbours.from', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='neighbours', full_name='protocol.Neighbours.neighbours', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='protocol.Neighbours.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=380,
  serialized_end=485,
)


_BACKUPMESSAGE = _descriptor.Descriptor(
  name='BackupMessage',
  full_name='protocol.BackupMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flag', full_name='protocol.BackupMessage.flag', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='priority', full_name='protocol.BackupMessage.priority', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=487,
  serialized_end=534,
)

_PINGMESSAGE.fields_by_name['from'].message_type = _ENDPOINT
_PINGMESSAGE.fields_by_name['to'].message_type = _ENDPOINT
_PONGMESSAGE.fields_by_name['from'].message_type = _ENDPOINT
_FINDNEIGHBOURS.fields_by_name['from'].message_type = _ENDPOINT
_NEIGHBOURS.fields_by_name['from'].message_type = _ENDPOINT
_NEIGHBOURS.fields_by_name['neighbours'].message_type = _ENDPOINT
DESCRIPTOR.message_types_by_name['Endpoint'] = _ENDPOINT
DESCRIPTOR.message_types_by_name['PingMessage'] = _PINGMESSAGE
DESCRIPTOR.message_types_by_name['PongMessage'] = _PONGMESSAGE
DESCRIPTOR.message_types_by_name['FindNeighbours'] = _FINDNEIGHBOURS
DESCRIPTOR.message_types_by_name['Neighbours'] = _NEIGHBOURS
DESCRIPTOR.message_types_by_name['BackupMessage'] = _BACKUPMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Endpoint = _reflection.GeneratedProtocolMessageType('Endpoint', (_message.Message,), {
  'DESCRIPTOR' : _ENDPOINT,
  '__module__' : 'core.Discover_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Endpoint)
  })
_sym_db.RegisterMessage(Endpoint)

PingMessage = _reflection.GeneratedProtocolMessageType('PingMessage', (_message.Message,), {
  'DESCRIPTOR' : _PINGMESSAGE,
  '__module__' : 'core.Discover_pb2'
  # @@protoc_insertion_point(class_scope:protocol.PingMessage)
  })
_sym_db.RegisterMessage(PingMessage)

PongMessage = _reflection.GeneratedProtocolMessageType('PongMessage', (_message.Message,), {
  'DESCRIPTOR' : _PONGMESSAGE,
  '__module__' : 'core.Discover_pb2'
  # @@protoc_insertion_point(class_scope:protocol.PongMessage)
  })
_sym_db.RegisterMessage(PongMessage)

FindNeighbours = _reflection.GeneratedProtocolMessageType('FindNeighbours', (_message.Message,), {
  'DESCRIPTOR' : _FINDNEIGHBOURS,
  '__module__' : 'core.Discover_pb2'
  # @@protoc_insertion_point(class_scope:protocol.FindNeighbours)
  })
_sym_db.RegisterMessage(FindNeighbours)

Neighbours = _reflection.GeneratedProtocolMessageType('Neighbours', (_message.Message,), {
  'DESCRIPTOR' : _NEIGHBOURS,
  '__module__' : 'core.Discover_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Neighbours)
  })
_sym_db.RegisterMessage(Neighbours)

BackupMessage = _reflection.GeneratedProtocolMessageType('BackupMessage', (_message.Message,), {
  'DESCRIPTOR' : _BACKUPMESSAGE,
  '__module__' : 'core.Discover_pb2'
  # @@protoc_insertion_point(class_scope:protocol.BackupMessage)
  })
_sym_db.RegisterMessage(BackupMessage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

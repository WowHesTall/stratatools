# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cartridge.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cartridge.proto',
  package='stratatools',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x63\x61rtridge.proto\x12\x0bstratatools\x1a\x1fgoogle/protobuf/timestamp.proto\"\xbf\x02\n\tCartridge\x12\x15\n\rserial_number\x18\x01 \x01(\x02\x12\x15\n\rmaterial_name\x18\x02 \x01(\t\x12\x19\n\x11manufacturing_lot\x18\x03 \x01(\t\x12\x36\n\x12manufacturing_date\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rlast_use_date\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12!\n\x19initial_material_quantity\x18\x06 \x01(\x02\x12!\n\x19\x63urrent_material_quantity\x18\x07 \x01(\x02\x12\x14\n\x0ckey_fragment\x18\x08 \x01(\x0c\x12\x0f\n\x07version\x18\t \x01(\r\x12\x11\n\tsignature\x18\n \x01(\tb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_CARTRIDGE = _descriptor.Descriptor(
  name='Cartridge',
  full_name='stratatools.Cartridge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serial_number', full_name='stratatools.Cartridge.serial_number', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='material_name', full_name='stratatools.Cartridge.material_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manufacturing_lot', full_name='stratatools.Cartridge.manufacturing_lot', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manufacturing_date', full_name='stratatools.Cartridge.manufacturing_date', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_use_date', full_name='stratatools.Cartridge.last_use_date', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial_material_quantity', full_name='stratatools.Cartridge.initial_material_quantity', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_material_quantity', full_name='stratatools.Cartridge.current_material_quantity', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key_fragment', full_name='stratatools.Cartridge.key_fragment', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='stratatools.Cartridge.version', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='stratatools.Cartridge.signature', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=385,
)

_CARTRIDGE.fields_by_name['manufacturing_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CARTRIDGE.fields_by_name['last_use_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Cartridge'] = _CARTRIDGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Cartridge = _reflection.GeneratedProtocolMessageType('Cartridge', (_message.Message,), dict(
  DESCRIPTOR = _CARTRIDGE,
  __module__ = 'cartridge_pb2'
  # @@protoc_insertion_point(class_scope:stratatools.Cartridge)
  ))
_sym_db.RegisterMessage(Cartridge)


# @@protoc_insertion_point(module_scope)

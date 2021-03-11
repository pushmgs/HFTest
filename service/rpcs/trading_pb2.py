# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trading.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import base_pb2 as base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='trading.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rtrading.proto\x1a\nbase.proto\"_\n\x0ePlaceTradeData\x12\x0c\n\x04time\x18\x01 \x01(\x04\x12\x1f\n\x08security\x18\x02 \x01(\x0b\x32\r.SecurityBase\x12\x0c\n\x04side\x18\x03 \x01(\r\x12\x10\n\x08quantity\x18\x04 \x01(\rb\x06proto3'
  ,
  dependencies=[base__pb2.DESCRIPTOR,])




_PLACETRADEDATA = _descriptor.Descriptor(
  name='PlaceTradeData',
  full_name='PlaceTradeData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='PlaceTradeData.time', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='security', full_name='PlaceTradeData.security', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='side', full_name='PlaceTradeData.side', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='PlaceTradeData.quantity', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=29,
  serialized_end=124,
)

_PLACETRADEDATA.fields_by_name['security'].message_type = base__pb2._SECURITYBASE
DESCRIPTOR.message_types_by_name['PlaceTradeData'] = _PLACETRADEDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlaceTradeData = _reflection.GeneratedProtocolMessageType('PlaceTradeData', (_message.Message,), {
  'DESCRIPTOR' : _PLACETRADEDATA,
  '__module__' : 'trading_pb2'
  # @@protoc_insertion_point(class_scope:PlaceTradeData)
  })
_sym_db.RegisterMessage(PlaceTradeData)


# @@protoc_insertion_point(module_scope)
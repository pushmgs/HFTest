# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: market.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='market.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cmarket.proto\"3\n\x12MarketDataResponse\x12\x0e\n\x06ticker\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\";\n\x11MarketDataRequest\x12\x0e\n\x06ticker\x18\x01 \x01(\t\x12\x16\n\x0estarting_value\x18\x02 \x01(\x02\x32N\n\rMarketService\x12=\n\x0eSendMarketData\x12\x12.MarketDataRequest\x1a\x13.MarketDataResponse\"\x00\x30\x01\x62\x06proto3'
)




_MARKETDATARESPONSE = _descriptor.Descriptor(
  name='MarketDataResponse',
  full_name='MarketDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ticker', full_name='MarketDataResponse.ticker', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='MarketDataResponse.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=16,
  serialized_end=67,
)


_MARKETDATAREQUEST = _descriptor.Descriptor(
  name='MarketDataRequest',
  full_name='MarketDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ticker', full_name='MarketDataRequest.ticker', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='starting_value', full_name='MarketDataRequest.starting_value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=69,
  serialized_end=128,
)

DESCRIPTOR.message_types_by_name['MarketDataResponse'] = _MARKETDATARESPONSE
DESCRIPTOR.message_types_by_name['MarketDataRequest'] = _MARKETDATAREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MarketDataResponse = _reflection.GeneratedProtocolMessageType('MarketDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _MARKETDATARESPONSE,
  '__module__' : 'market_pb2'
  # @@protoc_insertion_point(class_scope:MarketDataResponse)
  })
_sym_db.RegisterMessage(MarketDataResponse)

MarketDataRequest = _reflection.GeneratedProtocolMessageType('MarketDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _MARKETDATAREQUEST,
  '__module__' : 'market_pb2'
  # @@protoc_insertion_point(class_scope:MarketDataRequest)
  })
_sym_db.RegisterMessage(MarketDataRequest)



_MARKETSERVICE = _descriptor.ServiceDescriptor(
  name='MarketService',
  full_name='MarketService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=130,
  serialized_end=208,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendMarketData',
    full_name='MarketService.SendMarketData',
    index=0,
    containing_service=None,
    input_type=_MARKETDATAREQUEST,
    output_type=_MARKETDATARESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MARKETSERVICE)

DESCRIPTOR.services_by_name['MarketService'] = _MARKETSERVICE

# @@protoc_insertion_point(module_scope)

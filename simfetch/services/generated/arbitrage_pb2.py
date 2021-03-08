# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arbitrage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='arbitrage.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x61rbitrage.proto\"F\n\x18\x43urrencyArbitrageRequest\x12\x17\n\x0fnum_simulations\x18\x01 \x01(\r\x12\x11\n\tfix_after\x18\x02 \x01(\x08\"*\n\x11\x46\x65tchRatesRequest\x12\x15\n\rexchange_name\x18\x01 \x01(\t\"B\n\rRatesResponse\x12\x0c\n\x04\x62\x61nk\x18\x01 \x01(\t\x12\x15\n\rexchange_name\x18\x02 \x01(\t\x12\x0c\n\x04rate\x18\x03 \x01(\x01\x32\xa0\x01\n\x13\x41rbitrageSimulation\x12H\n\x17StreamCurrencyArbitrage\x12\x19.CurrencyArbitrageRequest\x1a\x0e.RatesResponse\"\x00\x30\x01\x12?\n\x13\x46\x65tchRatesFromCache\x12\x12.FetchRatesRequest\x1a\x0e.RatesResponse\"\x00(\x01\x30\x01\x62\x06proto3'
)




_CURRENCYARBITRAGEREQUEST = _descriptor.Descriptor(
  name='CurrencyArbitrageRequest',
  full_name='CurrencyArbitrageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_simulations', full_name='CurrencyArbitrageRequest.num_simulations', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fix_after', full_name='CurrencyArbitrageRequest.fix_after', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=19,
  serialized_end=89,
)


_FETCHRATESREQUEST = _descriptor.Descriptor(
  name='FetchRatesRequest',
  full_name='FetchRatesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='exchange_name', full_name='FetchRatesRequest.exchange_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=91,
  serialized_end=133,
)


_RATESRESPONSE = _descriptor.Descriptor(
  name='RatesResponse',
  full_name='RatesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bank', full_name='RatesResponse.bank', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exchange_name', full_name='RatesResponse.exchange_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate', full_name='RatesResponse.rate', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  serialized_start=135,
  serialized_end=201,
)

DESCRIPTOR.message_types_by_name['CurrencyArbitrageRequest'] = _CURRENCYARBITRAGEREQUEST
DESCRIPTOR.message_types_by_name['FetchRatesRequest'] = _FETCHRATESREQUEST
DESCRIPTOR.message_types_by_name['RatesResponse'] = _RATESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CurrencyArbitrageRequest = _reflection.GeneratedProtocolMessageType('CurrencyArbitrageRequest', (_message.Message,), {
  'DESCRIPTOR' : _CURRENCYARBITRAGEREQUEST,
  '__module__' : 'arbitrage_pb2'
  # @@protoc_insertion_point(class_scope:CurrencyArbitrageRequest)
  })
_sym_db.RegisterMessage(CurrencyArbitrageRequest)

FetchRatesRequest = _reflection.GeneratedProtocolMessageType('FetchRatesRequest', (_message.Message,), {
  'DESCRIPTOR' : _FETCHRATESREQUEST,
  '__module__' : 'arbitrage_pb2'
  # @@protoc_insertion_point(class_scope:FetchRatesRequest)
  })
_sym_db.RegisterMessage(FetchRatesRequest)

RatesResponse = _reflection.GeneratedProtocolMessageType('RatesResponse', (_message.Message,), {
  'DESCRIPTOR' : _RATESRESPONSE,
  '__module__' : 'arbitrage_pb2'
  # @@protoc_insertion_point(class_scope:RatesResponse)
  })
_sym_db.RegisterMessage(RatesResponse)



_ARBITRAGESIMULATION = _descriptor.ServiceDescriptor(
  name='ArbitrageSimulation',
  full_name='ArbitrageSimulation',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=204,
  serialized_end=364,
  methods=[
  _descriptor.MethodDescriptor(
    name='StreamCurrencyArbitrage',
    full_name='ArbitrageSimulation.StreamCurrencyArbitrage',
    index=0,
    containing_service=None,
    input_type=_CURRENCYARBITRAGEREQUEST,
    output_type=_RATESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FetchRatesFromCache',
    full_name='ArbitrageSimulation.FetchRatesFromCache',
    index=1,
    containing_service=None,
    input_type=_FETCHRATESREQUEST,
    output_type=_RATESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ARBITRAGESIMULATION)

DESCRIPTOR.services_by_name['ArbitrageSimulation'] = _ARBITRAGESIMULATION

# @@protoc_insertion_point(module_scope)
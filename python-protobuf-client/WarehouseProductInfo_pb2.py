# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WarehouseProductInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WarehouseProductInfo.proto',
  package='example',
  syntax='proto3',
  serialized_pb=_b('\n\x1aWarehouseProductInfo.proto\x12\x07\x65xample\"(\n\x14WarehouseProductInfo\x12\x10\n\x08quantity\x18\x01 \x01(\x05\x42\x34\n\x17\x63om.example.protocolbufB\x19WarehouseProductInfoProtob\x06proto3')
)




_WAREHOUSEPRODUCTINFO = _descriptor.Descriptor(
  name='WarehouseProductInfo',
  full_name='example.WarehouseProductInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quantity', full_name='example.WarehouseProductInfo.quantity', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=39,
  serialized_end=79,
)

DESCRIPTOR.message_types_by_name['WarehouseProductInfo'] = _WAREHOUSEPRODUCTINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WarehouseProductInfo = _reflection.GeneratedProtocolMessageType('WarehouseProductInfo', (_message.Message,), dict(
  DESCRIPTOR = _WAREHOUSEPRODUCTINFO,
  __module__ = 'WarehouseProductInfo_pb2'
  # @@protoc_insertion_point(class_scope:example.WarehouseProductInfo)
  ))
_sym_db.RegisterMessage(WarehouseProductInfo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\027com.example.protocolbufB\031WarehouseProductInfoProto'))
# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Importer.proto

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
  name='Importer.proto',
  package='example',
  syntax='proto3',
  serialized_pb=_b('\n\x0eImporter.proto\x12\x07\x65xample\"\x18\n\x08Importer\x12\x0c\n\x04name\x18\x01 \x01(\tB(\n\x17\x63om.example.protocolbufB\rImporterProtob\x06proto3')
)




_IMPORTER = _descriptor.Descriptor(
  name='Importer',
  full_name='example.Importer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='example.Importer.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=27,
  serialized_end=51,
)

DESCRIPTOR.message_types_by_name['Importer'] = _IMPORTER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Importer = _reflection.GeneratedProtocolMessageType('Importer', (_message.Message,), dict(
  DESCRIPTOR = _IMPORTER,
  __module__ = 'Importer_pb2'
  # @@protoc_insertion_point(class_scope:example.Importer)
  ))
_sym_db.RegisterMessage(Importer)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\027com.example.protocolbufB\rImporterProto'))
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: my.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='my.proto',
  package='grpc_stream_x2',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x08my.proto\x12\x0egrpc_stream_x2\"U\n\x0b\x46ileRequest\x12\x0f\n\x07image_1\x18\x01 \x01(\x0c\x12\x0f\n\x07image_2\x18\x02 \x01(\x0c\x12\x11\n\tfilename1\x18\x03 \x01(\t\x12\x11\n\tfilename2\x18\x04 \x01(\t\";\n\x0c\x42\x61tchRequest\x12+\n\x06images\x18\x01 \x03(\x0b\x32\x1b.grpc_stream_x2.FileRequest\"\x1f\n\x0c\x46ileResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xa2\x01\n\x13\x46ileTransferService\x12\x46\n\x05\x43\x61se4\x12\x1b.grpc_stream_x2.FileRequest\x1a\x1c.grpc_stream_x2.FileResponse(\x01\x30\x01\x12\x43\n\x05\x43\x61se5\x12\x1c.grpc_stream_x2.BatchRequest\x1a\x1c.grpc_stream_x2.FileResponseb\x06proto3'
)




_FILEREQUEST = _descriptor.Descriptor(
  name='FileRequest',
  full_name='grpc_stream_x2.FileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image_1', full_name='grpc_stream_x2.FileRequest.image_1', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image_2', full_name='grpc_stream_x2.FileRequest.image_2', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filename1', full_name='grpc_stream_x2.FileRequest.filename1', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filename2', full_name='grpc_stream_x2.FileRequest.filename2', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=28,
  serialized_end=113,
)


_BATCHREQUEST = _descriptor.Descriptor(
  name='BatchRequest',
  full_name='grpc_stream_x2.BatchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='images', full_name='grpc_stream_x2.BatchRequest.images', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=115,
  serialized_end=174,
)


_FILERESPONSE = _descriptor.Descriptor(
  name='FileResponse',
  full_name='grpc_stream_x2.FileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='grpc_stream_x2.FileResponse.message', index=0,
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
  serialized_start=176,
  serialized_end=207,
)

_BATCHREQUEST.fields_by_name['images'].message_type = _FILEREQUEST
DESCRIPTOR.message_types_by_name['FileRequest'] = _FILEREQUEST
DESCRIPTOR.message_types_by_name['BatchRequest'] = _BATCHREQUEST
DESCRIPTOR.message_types_by_name['FileResponse'] = _FILERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FileRequest = _reflection.GeneratedProtocolMessageType('FileRequest', (_message.Message,), {
  'DESCRIPTOR' : _FILEREQUEST,
  '__module__' : 'my_pb2'
  # @@protoc_insertion_point(class_scope:grpc_stream_x2.FileRequest)
  })
_sym_db.RegisterMessage(FileRequest)

BatchRequest = _reflection.GeneratedProtocolMessageType('BatchRequest', (_message.Message,), {
  'DESCRIPTOR' : _BATCHREQUEST,
  '__module__' : 'my_pb2'
  # @@protoc_insertion_point(class_scope:grpc_stream_x2.BatchRequest)
  })
_sym_db.RegisterMessage(BatchRequest)

FileResponse = _reflection.GeneratedProtocolMessageType('FileResponse', (_message.Message,), {
  'DESCRIPTOR' : _FILERESPONSE,
  '__module__' : 'my_pb2'
  # @@protoc_insertion_point(class_scope:grpc_stream_x2.FileResponse)
  })
_sym_db.RegisterMessage(FileResponse)



_FILETRANSFERSERVICE = _descriptor.ServiceDescriptor(
  name='FileTransferService',
  full_name='grpc_stream_x2.FileTransferService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=210,
  serialized_end=372,
  methods=[
  _descriptor.MethodDescriptor(
    name='Case4',
    full_name='grpc_stream_x2.FileTransferService.Case4',
    index=0,
    containing_service=None,
    input_type=_FILEREQUEST,
    output_type=_FILERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Case5',
    full_name='grpc_stream_x2.FileTransferService.Case5',
    index=1,
    containing_service=None,
    input_type=_BATCHREQUEST,
    output_type=_FILERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FILETRANSFERSERVICE)

DESCRIPTOR.services_by_name['FileTransferService'] = _FILETRANSFERSERVICE

# @@protoc_insertion_point(module_scope)
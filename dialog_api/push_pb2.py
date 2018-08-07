# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: push.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
import definitions_pb2 as definitions__pb2
import miscellaneous_pb2 as miscellaneous__pb2
from scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='push.proto',
  package='dialog',
  syntax='proto3',
  serialized_pb=_b('\n\npush.proto\x12\x06\x64ialog\x1a\x1cgoogle/api/annotations.proto\x1a\x11\x64\x65\x66initions.proto\x1a\x13miscellaneous.proto\x1a\x15scalapb/scalapb.proto\"x\n\x19RequestRegisterGooglePush\x12 \n\nproject_id\x18\x01 \x01(\x03\x42\x0c\x8a\xea\x30\x08\n\x06hidden\x12\x1b\n\x05token\x18\x02 \x01(\tB\x0c\x8a\xea\x30\x08\n\x06hidden:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"X\n\x1bRequestUnregisterGooglePush\x12\x1b\n\x05token\x18\x01 \x01(\tB\x0c\x8a\xea\x30\x08\n\x06hidden:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"v\n\x18RequestRegisterApplePush\x12\x1f\n\x08\x61pns_key\x18\x01 \x01(\x05\x42\r\x8a\xea\x30\t\n\x07visible\x12\x1b\n\x05token\x18\x02 \x01(\tB\x0c\x8a\xea\x30\x08\n\x06hidden:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"W\n\x1aRequestUnregisterApplePush\x12\x1b\n\x05token\x18\x01 \x01(\tB\x0c\x8a\xea\x30\x08\n\x06hidden:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"y\n\x1bRequestRegisterApplePushKit\x12\x1f\n\x08\x61pns_key\x18\x01 \x01(\x05\x42\r\x8a\xea\x30\t\n\x07visible\x12\x1b\n\x05token\x18\x02 \x01(\tB\x0c\x8a\xea\x30\x08\n\x06hidden:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"Z\n\x1dRequestUnregisterApplePushKit\x12\x1b\n\x05token\x18\x01 \x01(\tB\x0c\x8a\xea\x30\x08\n\x06hidden:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"|\n\x1dRequestRegisterApplePushToken\x12 \n\tbundle_id\x18\x01 \x01(\tB\r\x8a\xea\x30\t\n\x07visible\x12\x1b\n\x05token\x18\x02 \x01(\tB\x0c\x8a\xea\x30\x08\n\x06hidden:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"\\\n\x1fRequestUnregisterApplePushToken\x12\x1b\n\x05token\x18\x01 \x01(\tB\x0c\x8a\xea\x30\x08\n\x06hidden:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest2\xa1\x08\n\x04Push\x12z\n\x12RegisterGooglePush\x12!.dialog.RequestRegisterGooglePush\x1a\x14.dialog.ResponseVoid\"+\x82\xd3\xe4\x93\x02%\" /v1/grpc/Push/RegisterGooglePush:\x01*\x12\x80\x01\n\x14UnregisterGooglePush\x12#.dialog.RequestUnregisterGooglePush\x1a\x14.dialog.ResponseVoid\"-\x82\xd3\xe4\x93\x02\'\"\"/v1/grpc/Push/UnregisterGooglePush:\x01*\x12w\n\x11RegisterApplePush\x12 .dialog.RequestRegisterApplePush\x1a\x14.dialog.ResponseVoid\"*\x82\xd3\xe4\x93\x02$\"\x1f/v1/grpc/Push/RegisterApplePush:\x01*\x12}\n\x13UnregisterApplePush\x12\".dialog.RequestUnregisterApplePush\x1a\x14.dialog.ResponseVoid\",\x82\xd3\xe4\x93\x02&\"!/v1/grpc/Push/UnregisterApplePush:\x01*\x12\x80\x01\n\x14RegisterApplePushKit\x12#.dialog.RequestRegisterApplePushKit\x1a\x14.dialog.ResponseVoid\"-\x82\xd3\xe4\x93\x02\'\"\"/v1/grpc/Push/RegisterApplePushKit:\x01*\x12\x86\x01\n\x16UnregisterApplePushKit\x12%.dialog.RequestUnregisterApplePushKit\x1a\x14.dialog.ResponseVoid\"/\x82\xd3\xe4\x93\x02)\"$/v1/grpc/Push/UnregisterApplePushKit:\x01*\x12\x86\x01\n\x16RegisterApplePushToken\x12%.dialog.RequestRegisterApplePushToken\x1a\x14.dialog.ResponseVoid\"/\x82\xd3\xe4\x93\x02)\"$/v1/grpc/Push/RegisterApplePushToken:\x01*\x12\x8c\x01\n\x18UnregisterApplePushToken\x12\'.dialog.RequestUnregisterApplePushToken\x1a\x14.dialog.ResponseVoid\"1\x82\xd3\xe4\x93\x02+\"&/v1/grpc/Push/UnregisterApplePushToken:\x01*B\x19\xe2?\x16\n\x14im.dlg.grpc.servicesb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,definitions__pb2.DESCRIPTOR,miscellaneous__pb2.DESCRIPTOR,scalapb_dot_scalapb__pb2.DESCRIPTOR,])




_REQUESTREGISTERGOOGLEPUSH = _descriptor.Descriptor(
  name='RequestRegisterGooglePush',
  full_name='dialog.RequestRegisterGooglePush',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='dialog.RequestRegisterGooglePush.project_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\010\n\006hidden')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='dialog.RequestRegisterGooglePush.token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\010\n\006hidden')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\342?\031\n\027im.dlg.grpc.GrpcRequest')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=235,
)


_REQUESTUNREGISTERGOOGLEPUSH = _descriptor.Descriptor(
  name='RequestUnregisterGooglePush',
  full_name='dialog.RequestUnregisterGooglePush',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='dialog.RequestUnregisterGooglePush.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\010\n\006hidden')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\342?\031\n\027im.dlg.grpc.GrpcRequest')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=237,
  serialized_end=325,
)


_REQUESTREGISTERAPPLEPUSH = _descriptor.Descriptor(
  name='RequestRegisterApplePush',
  full_name='dialog.RequestRegisterApplePush',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='apns_key', full_name='dialog.RequestRegisterApplePush.apns_key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='dialog.RequestRegisterApplePush.token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\010\n\006hidden')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\342?\031\n\027im.dlg.grpc.GrpcRequest')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=327,
  serialized_end=445,
)


_REQUESTUNREGISTERAPPLEPUSH = _descriptor.Descriptor(
  name='RequestUnregisterApplePush',
  full_name='dialog.RequestUnregisterApplePush',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='dialog.RequestUnregisterApplePush.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\010\n\006hidden')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\342?\031\n\027im.dlg.grpc.GrpcRequest')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=447,
  serialized_end=534,
)


_REQUESTREGISTERAPPLEPUSHKIT = _descriptor.Descriptor(
  name='RequestRegisterApplePushKit',
  full_name='dialog.RequestRegisterApplePushKit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='apns_key', full_name='dialog.RequestRegisterApplePushKit.apns_key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='dialog.RequestRegisterApplePushKit.token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\010\n\006hidden')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\342?\031\n\027im.dlg.grpc.GrpcRequest')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=536,
  serialized_end=657,
)


_REQUESTUNREGISTERAPPLEPUSHKIT = _descriptor.Descriptor(
  name='RequestUnregisterApplePushKit',
  full_name='dialog.RequestUnregisterApplePushKit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='dialog.RequestUnregisterApplePushKit.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\010\n\006hidden')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\342?\031\n\027im.dlg.grpc.GrpcRequest')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=659,
  serialized_end=749,
)


_REQUESTREGISTERAPPLEPUSHTOKEN = _descriptor.Descriptor(
  name='RequestRegisterApplePushToken',
  full_name='dialog.RequestRegisterApplePushToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bundle_id', full_name='dialog.RequestRegisterApplePushToken.bundle_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='dialog.RequestRegisterApplePushToken.token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\010\n\006hidden')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\342?\031\n\027im.dlg.grpc.GrpcRequest')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=751,
  serialized_end=875,
)


_REQUESTUNREGISTERAPPLEPUSHTOKEN = _descriptor.Descriptor(
  name='RequestUnregisterApplePushToken',
  full_name='dialog.RequestUnregisterApplePushToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='dialog.RequestUnregisterApplePushToken.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\010\n\006hidden')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\342?\031\n\027im.dlg.grpc.GrpcRequest')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=877,
  serialized_end=969,
)

DESCRIPTOR.message_types_by_name['RequestRegisterGooglePush'] = _REQUESTREGISTERGOOGLEPUSH
DESCRIPTOR.message_types_by_name['RequestUnregisterGooglePush'] = _REQUESTUNREGISTERGOOGLEPUSH
DESCRIPTOR.message_types_by_name['RequestRegisterApplePush'] = _REQUESTREGISTERAPPLEPUSH
DESCRIPTOR.message_types_by_name['RequestUnregisterApplePush'] = _REQUESTUNREGISTERAPPLEPUSH
DESCRIPTOR.message_types_by_name['RequestRegisterApplePushKit'] = _REQUESTREGISTERAPPLEPUSHKIT
DESCRIPTOR.message_types_by_name['RequestUnregisterApplePushKit'] = _REQUESTUNREGISTERAPPLEPUSHKIT
DESCRIPTOR.message_types_by_name['RequestRegisterApplePushToken'] = _REQUESTREGISTERAPPLEPUSHTOKEN
DESCRIPTOR.message_types_by_name['RequestUnregisterApplePushToken'] = _REQUESTUNREGISTERAPPLEPUSHTOKEN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestRegisterGooglePush = _reflection.GeneratedProtocolMessageType('RequestRegisterGooglePush', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTREGISTERGOOGLEPUSH,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestRegisterGooglePush)
  ))
_sym_db.RegisterMessage(RequestRegisterGooglePush)

RequestUnregisterGooglePush = _reflection.GeneratedProtocolMessageType('RequestUnregisterGooglePush', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTUNREGISTERGOOGLEPUSH,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestUnregisterGooglePush)
  ))
_sym_db.RegisterMessage(RequestUnregisterGooglePush)

RequestRegisterApplePush = _reflection.GeneratedProtocolMessageType('RequestRegisterApplePush', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTREGISTERAPPLEPUSH,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestRegisterApplePush)
  ))
_sym_db.RegisterMessage(RequestRegisterApplePush)

RequestUnregisterApplePush = _reflection.GeneratedProtocolMessageType('RequestUnregisterApplePush', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTUNREGISTERAPPLEPUSH,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestUnregisterApplePush)
  ))
_sym_db.RegisterMessage(RequestUnregisterApplePush)

RequestRegisterApplePushKit = _reflection.GeneratedProtocolMessageType('RequestRegisterApplePushKit', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTREGISTERAPPLEPUSHKIT,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestRegisterApplePushKit)
  ))
_sym_db.RegisterMessage(RequestRegisterApplePushKit)

RequestUnregisterApplePushKit = _reflection.GeneratedProtocolMessageType('RequestUnregisterApplePushKit', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTUNREGISTERAPPLEPUSHKIT,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestUnregisterApplePushKit)
  ))
_sym_db.RegisterMessage(RequestUnregisterApplePushKit)

RequestRegisterApplePushToken = _reflection.GeneratedProtocolMessageType('RequestRegisterApplePushToken', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTREGISTERAPPLEPUSHTOKEN,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestRegisterApplePushToken)
  ))
_sym_db.RegisterMessage(RequestRegisterApplePushToken)

RequestUnregisterApplePushToken = _reflection.GeneratedProtocolMessageType('RequestUnregisterApplePushToken', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTUNREGISTERAPPLEPUSHTOKEN,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestUnregisterApplePushToken)
  ))
_sym_db.RegisterMessage(RequestUnregisterApplePushToken)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\342?\026\n\024im.dlg.grpc.services'))
_REQUESTREGISTERGOOGLEPUSH.fields_by_name['project_id'].has_options = True
_REQUESTREGISTERGOOGLEPUSH.fields_by_name['project_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\010\n\006hidden'))
_REQUESTREGISTERGOOGLEPUSH.fields_by_name['token'].has_options = True
_REQUESTREGISTERGOOGLEPUSH.fields_by_name['token']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\010\n\006hidden'))
_REQUESTREGISTERGOOGLEPUSH.has_options = True
_REQUESTREGISTERGOOGLEPUSH._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\342?\031\n\027im.dlg.grpc.GrpcRequest'))
_REQUESTUNREGISTERGOOGLEPUSH.fields_by_name['token'].has_options = True
_REQUESTUNREGISTERGOOGLEPUSH.fields_by_name['token']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\010\n\006hidden'))
_REQUESTUNREGISTERGOOGLEPUSH.has_options = True
_REQUESTUNREGISTERGOOGLEPUSH._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\342?\031\n\027im.dlg.grpc.GrpcRequest'))
_REQUESTREGISTERAPPLEPUSH.fields_by_name['apns_key'].has_options = True
_REQUESTREGISTERAPPLEPUSH.fields_by_name['apns_key']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible'))
_REQUESTREGISTERAPPLEPUSH.fields_by_name['token'].has_options = True
_REQUESTREGISTERAPPLEPUSH.fields_by_name['token']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\010\n\006hidden'))
_REQUESTREGISTERAPPLEPUSH.has_options = True
_REQUESTREGISTERAPPLEPUSH._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\342?\031\n\027im.dlg.grpc.GrpcRequest'))
_REQUESTUNREGISTERAPPLEPUSH.fields_by_name['token'].has_options = True
_REQUESTUNREGISTERAPPLEPUSH.fields_by_name['token']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\010\n\006hidden'))
_REQUESTUNREGISTERAPPLEPUSH.has_options = True
_REQUESTUNREGISTERAPPLEPUSH._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\342?\031\n\027im.dlg.grpc.GrpcRequest'))
_REQUESTREGISTERAPPLEPUSHKIT.fields_by_name['apns_key'].has_options = True
_REQUESTREGISTERAPPLEPUSHKIT.fields_by_name['apns_key']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible'))
_REQUESTREGISTERAPPLEPUSHKIT.fields_by_name['token'].has_options = True
_REQUESTREGISTERAPPLEPUSHKIT.fields_by_name['token']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\010\n\006hidden'))
_REQUESTREGISTERAPPLEPUSHKIT.has_options = True
_REQUESTREGISTERAPPLEPUSHKIT._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\342?\031\n\027im.dlg.grpc.GrpcRequest'))
_REQUESTUNREGISTERAPPLEPUSHKIT.fields_by_name['token'].has_options = True
_REQUESTUNREGISTERAPPLEPUSHKIT.fields_by_name['token']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\010\n\006hidden'))
_REQUESTUNREGISTERAPPLEPUSHKIT.has_options = True
_REQUESTUNREGISTERAPPLEPUSHKIT._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\342?\031\n\027im.dlg.grpc.GrpcRequest'))
_REQUESTREGISTERAPPLEPUSHTOKEN.fields_by_name['bundle_id'].has_options = True
_REQUESTREGISTERAPPLEPUSHTOKEN.fields_by_name['bundle_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible'))
_REQUESTREGISTERAPPLEPUSHTOKEN.fields_by_name['token'].has_options = True
_REQUESTREGISTERAPPLEPUSHTOKEN.fields_by_name['token']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\010\n\006hidden'))
_REQUESTREGISTERAPPLEPUSHTOKEN.has_options = True
_REQUESTREGISTERAPPLEPUSHTOKEN._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\342?\031\n\027im.dlg.grpc.GrpcRequest'))
_REQUESTUNREGISTERAPPLEPUSHTOKEN.fields_by_name['token'].has_options = True
_REQUESTUNREGISTERAPPLEPUSHTOKEN.fields_by_name['token']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\010\n\006hidden'))
_REQUESTUNREGISTERAPPLEPUSHTOKEN.has_options = True
_REQUESTUNREGISTERAPPLEPUSHTOKEN._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\342?\031\n\027im.dlg.grpc.GrpcRequest'))

_PUSH = _descriptor.ServiceDescriptor(
  name='Push',
  full_name='dialog.Push',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=972,
  serialized_end=2029,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterGooglePush',
    full_name='dialog.Push.RegisterGooglePush',
    index=0,
    containing_service=None,
    input_type=_REQUESTREGISTERGOOGLEPUSH,
    output_type=miscellaneous__pb2._RESPONSEVOID,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002%\" /v1/grpc/Push/RegisterGooglePush:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='UnregisterGooglePush',
    full_name='dialog.Push.UnregisterGooglePush',
    index=1,
    containing_service=None,
    input_type=_REQUESTUNREGISTERGOOGLEPUSH,
    output_type=miscellaneous__pb2._RESPONSEVOID,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\'\"\"/v1/grpc/Push/UnregisterGooglePush:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='RegisterApplePush',
    full_name='dialog.Push.RegisterApplePush',
    index=2,
    containing_service=None,
    input_type=_REQUESTREGISTERAPPLEPUSH,
    output_type=miscellaneous__pb2._RESPONSEVOID,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002$\"\037/v1/grpc/Push/RegisterApplePush:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='UnregisterApplePush',
    full_name='dialog.Push.UnregisterApplePush',
    index=3,
    containing_service=None,
    input_type=_REQUESTUNREGISTERAPPLEPUSH,
    output_type=miscellaneous__pb2._RESPONSEVOID,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002&\"!/v1/grpc/Push/UnregisterApplePush:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='RegisterApplePushKit',
    full_name='dialog.Push.RegisterApplePushKit',
    index=4,
    containing_service=None,
    input_type=_REQUESTREGISTERAPPLEPUSHKIT,
    output_type=miscellaneous__pb2._RESPONSEVOID,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\'\"\"/v1/grpc/Push/RegisterApplePushKit:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='UnregisterApplePushKit',
    full_name='dialog.Push.UnregisterApplePushKit',
    index=5,
    containing_service=None,
    input_type=_REQUESTUNREGISTERAPPLEPUSHKIT,
    output_type=miscellaneous__pb2._RESPONSEVOID,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002)\"$/v1/grpc/Push/UnregisterApplePushKit:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='RegisterApplePushToken',
    full_name='dialog.Push.RegisterApplePushToken',
    index=6,
    containing_service=None,
    input_type=_REQUESTREGISTERAPPLEPUSHTOKEN,
    output_type=miscellaneous__pb2._RESPONSEVOID,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002)\"$/v1/grpc/Push/RegisterApplePushToken:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='UnregisterApplePushToken',
    full_name='dialog.Push.UnregisterApplePushToken',
    index=7,
    containing_service=None,
    input_type=_REQUESTUNREGISTERAPPLEPUSHTOKEN,
    output_type=miscellaneous__pb2._RESPONSEVOID,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002+\"&/v1/grpc/Push/UnregisterApplePushToken:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_PUSH)

DESCRIPTOR.services_by_name['Push'] = _PUSH

# @@protoc_insertion_point(module_scope)

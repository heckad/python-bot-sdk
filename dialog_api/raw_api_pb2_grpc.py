# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import raw_api_pb2 as raw__api__pb2


class RawAPIStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RawRequest = channel.unary_unary(
        '/dialog.RawAPI/RawRequest',
        request_serializer=raw__api__pb2.RequestRawRequest.SerializeToString,
        response_deserializer=raw__api__pb2.ResponseRawRequest.FromString,
        )


class RawAPIServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def RawRequest(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RawAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RawRequest': grpc.unary_unary_rpc_method_handler(
          servicer.RawRequest,
          request_deserializer=raw__api__pb2.RequestRawRequest.FromString,
          response_serializer=raw__api__pb2.ResponseRawRequest.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dialog.RawAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import market_pb2 as market__pb2


class MarketServiceStub(object):
    """Market service definition
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendMarketData = channel.unary_stream(
                '/MarketService/SendMarketData',
                request_serializer=market__pb2.MarketDataRequest.SerializeToString,
                response_deserializer=market__pb2.MarketDataResponse.FromString,
                )


class MarketServiceServicer(object):
    """Market service definition
    """

    def SendMarketData(self, request, context):
        """Sends generated market data back, whether historical or randomly generated data.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MarketServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendMarketData': grpc.unary_stream_rpc_method_handler(
                    servicer.SendMarketData,
                    request_deserializer=market__pb2.MarketDataRequest.FromString,
                    response_serializer=market__pb2.MarketDataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MarketService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MarketService(object):
    """Market service definition
    """

    @staticmethod
    def SendMarketData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/MarketService/SendMarketData',
            market__pb2.MarketDataRequest.SerializeToString,
            market__pb2.MarketDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
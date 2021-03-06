# HFTest - Written by Matt Smalley, Ronald Oliver and Jaimin Vyas

from concurrent import futures
import time
import logging

import grpc
from grpc_reflection.v1alpha import reflection

import market_pb2
import market_pb2_grpc

class MarketSimulationServicer(market_pb2_grpc.MarketSimulationServicer):
    """Handling implementation for market data requests."""
    
    def __init__(self):
        pass
    
    def CreateMarketStream(self, request, context) -> float:
        """
        Temporarily generate values (to the fourth decimal place)
        Just used for streaming demo with Evans
        """
        starting_value = request.starting_value
        response = market_pb2.MarketDataResponse(
            ticker = request.ticker, 
            value = request.starting_value)
        for i in range(request.num_tests):
            response.value = starting_value + (0.0001 * i)
            yield response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    market_pb2_grpc.add_MarketSimulationServicer_to_server(
        MarketSimulationServicer(), server)
    SERVICE_NAMES = (
        market_pb2.DESCRIPTOR.services_by_name['MarketSimulation'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('[::]:90091')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()


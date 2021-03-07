# HFTest - Written by Matt Smalley

from concurrent import futures
import time
import logging

import grpc
from grpc_reflection.v1alpha import reflection

import trade_simulation_pb2
import trade_simulation_pb2_grpc

class TradeSimulationServicer(trade_simulation_pb2_grpc.TradeSimulationServicer):
    """Trade streaming service implementation"""

    def __init__(self):
        pass

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    trade_simulation_pb2_grpc.add_TradeSimulationServicer_to_server(
        TradeSimulationServicer(), server)
    SERVICE_NAMES = (
        trade_simulation_pb2.DESCRIPTOR.services_by_name['TradeSimulation'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()


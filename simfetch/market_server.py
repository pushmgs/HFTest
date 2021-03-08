# HFTest - Written by Matt Smalley

from concurrent import futures
import time
import logging

import grpc
from grpc_reflection.v1alpha import reflection

import trading_pb2
import trading_pb2_grpc
from arbitrary import generate_arbitrary_currency_stream

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    trading_pb2_grpc.add_TradeSimulationServicer_to_server(
        TradeSimulationServicer(), server)
    SERVICE_NAMES = (
        trading_pb2.DESCRIPTOR.services_by_name['TradeSimulation'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()


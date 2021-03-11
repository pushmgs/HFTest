# HFTest - Written by Matt Smalley

from concurrent import futures
import time
import logging

import grpc
from grpc_reflection.v1alpha import reflection

import arbitrary_pb2
import arbitrary_pb2_grpc

import arbitrage_pb2
import arbitrage_pb2_grpc

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    
    # Add services
    arbitrage_pb2_grpc.add_ArbitrageSimulationServicer_to_server(
        arbitrage_pb2_grpc.ArbitrageSimulationServicer(), server)
    
    SERVICE_NAMES = (
        arbitrage_pb2.DESCRIPTOR.services_by_name['ArbitrageSimulation'].full_name,
        reflection.SERVICE_NAME,
    )

    # Enable reflection
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()


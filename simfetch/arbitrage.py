# Arbitrage generation functions

from trade_simulation_pb2_grpc import TradeArbitrageRequest, SecurityBase

def generate_arbitrage_data(request: TradeArbitrageRequest):
    securities = request.securities
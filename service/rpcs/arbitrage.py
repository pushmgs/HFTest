from base_pb2 import CurrencyBase
from arbitrage_pb2 import CurrencyArbitrageRequest, FetchRatesRequest, RatesResponse

import arbitrage_pb2_grpc

from util import truncate
from decimal import *
import random

class BankExchangeInformation:
    # Lightweight class, contains a bank and an exchange rate
    def __init__(self, bank: str=None, exchange_name: str, rate: Decimal=0.0):
        self.bank = bank
        self.exchange_name = exchange_name
        self.rate = rate
    
    def __str__(self):
        return self.exchange_name + ': ' + self.rate

class ArbitrageSimulationServicer(arbitrage_pb2_grpc.ArbitrageSimulationServicer):
    # Arbitrage simluation tools & stream implementations.

    def __init__(self):
        self.exchange_rates = dict()

    def FetchRatesFromCache(self, response, context):
        # Bi-directional streaming so that the client can send results from cache
        self.exchange_rates[response.exchange_name] = BankExchangeInformation(response.bank, response.exchange_name, response.rate)

    # Triangular Arbitrage method
    def StreamCurrencyArbitrage(self, request: CurrencyArbitrageRequest, context) -> RatesResponse:
        num_simulations = request.num_simulations
        arbitrage_iteration = random.randrange(0, num_simulations)
        fix_after = request.fix_after

        keys = set(self.exchange_rates.keys())
        exchanges = random.sample(keys, 3)
        arbitrage_rate = (self.exchange_rates[exchanges[0]].rate * self.exchange_rates[exchanges[2]].rate) - 0.0002 # Obvious enough

        response = RatesResponse()
        arbitrage_occured = False

        for i in range(num_simulations):
            if i == arbitrage_iteration:
                self.exchange_rates[exchanges[1]] = arbitrage_rate
                response.bank = self.exchange_rates[exchanges[1]].bank
                response.rate = arbitrage_rate
                yield response
            else:
                if arbitrage_occured:
                    if not fix_after:
                        return response
                    else:
                        random_exchange = random.rand_range(0, 2)
                        response.bank = self.exchange_rates[exchanges[random_exchange]].bank
                        response.rate = self.exchange_rates[exchanges[random_exchange]].rate
                        yield response
from generated.arbitrary_pb2 import CurrencyArbitraryRequest
from generated.base_pb2 import CurrencyBase
from util import truncate
import random

# Small fluctuations at the moment
def generate_arbitrary_currency_stream(request: CurrencyArbitraryRequest) -> CurrencyBase:
    currencies = request.currencies
    num_simulations = request.num_simulations

    # Generate randomly truncated value, multiply by 1 x 10^-10 & truncate to 10 decimal places.
    # Add (or subtract) that value to each currency
    for i in range(num_simulations):
        for currency in currencies:
            rand_key = random.choice(list(currency.sells_for))
            price = currency.sells_for[rand_key]
            a = random.randint(1, 9)
            negative_flag = bool(random.getrandbits(1))
            if negative_flag is False:
                price = truncate(price + (a * 0.0000000001), 10)
            else:
                price = truncate(price - (a * 0.0000000001), 10)
            currency.sells_for[rand_key] = price
            yield currency
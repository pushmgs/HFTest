# Random security generation functions

from trading_pb2 import CurrencyArbitraryRequest, CurrencyBase
import random

def truncate(number: float, digits: int) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

# Small fluctuations at the moment
def generate_arbitrary_currency_stream(request: CurrencyArbitraryRequest) -> CurrencyBase:
    currencies = request.currencies
    num_simulations = request.num_simulations

    # Generate randomly truncated value, multiply by 1 x 10^-10 & truncate to 10 decimal places.
    # Add (or subtract) that value to each currency
    for i in range(num_simulations):
        for currency in currencies:
            a = random.randint(1, 9)
            negative_flag = bool(random.getrandbits(1))
            if negative_flag is False:
                currency.price = truncate(currency.price + (a * 0.0000000001), 10)
            else:
                currency.price = truncate(currency.price - (a * 0.0000000001), 10)
            yield currency
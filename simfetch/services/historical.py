# Can fetch from either finance API or market data capture.

from generated.base_pb2 import SecurityBase, CurrencyBase
from generated.historical_pb2 import InstrumentHistoricalResponse
import json

# Assuming that the security id is already known since we're fetching from a file
def stream_instrument_json(filename: str) -> InstrumentHistoricalResponse:
    base = InstrumentHistoricalResponse()
    with open(filename, 'r') as designated_file:
        data = designated_file.read()
    security_data = json.loads(data)
    for entry in security_data:
        base.price = entry['price']
        base.time = entry['time']
        yield base

# Just returning here instead of having a generator.
def fetch_instrument_json(filename: str) -> []:
    responses = []
    with open(filename, 'r') as designated_file:
        data = designated_file.read()
    security_data = json.loads(data)
    for entry in security_data:
        base = InstrumentHistoricalResponse()
        base.price = entry['price']
        base.time = entry['time']
        responses.append(base)
    return responses

# Probably yahoo
def fetch_api(api_name: str):
    pass
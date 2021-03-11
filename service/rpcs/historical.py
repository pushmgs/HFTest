from base_pb2 import SecurityBase, CurrencyBase
from historical_pb2 import InstrumentHistoricalResponse

import historical_pb2_grpc

import json

class HistoricalSimulationServicer(historical_pb2_grpc.HistoricalSimulationServicer):
    # Service to stream historical data back to the codebase so that it can re-evaluate market capture
    # with newer strategies

    def __init__(self):
        pass

    def StreamSecurityHistory(self, request, context) -> InstrumentHistoricalResponse:
        read_json = True if request.file_path != "" else False
         # Unsure if causes gRPC clog
        if not read_json:
            yield InstrumentHistoricalResponse(price=0, time="DNE")

        # Stream for now
        instrument_history = _fetch_instrument_history(request.file_path)
        for value in instrument_history:
            yield value

    # Just returning here instead of having a generator.
    def _fetch_instrument_json(filename: str) -> []:
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

from resources.resistor.resistor import ResistorApi, ResistorColorApi
from resources.circuit.circuit import CircuitResistanceAll


def initialize_routes(api):
    api.add_resource(ResistorApi, '/api/resistor')

    api.add_resource(ResistorColorApi, '/api/color/<color>')

    api.add_resource(CircuitResistanceAll, '/api/resistance_all')



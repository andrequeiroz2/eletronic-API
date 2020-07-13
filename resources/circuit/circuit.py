from flask import Response, request, json
from flask_restful import Resource
from calculations.circuit.circuit_resistance import circuit


class CircuitResistanceAll(Resource):
    def post(self):
        body = request.get_json()
        result = circuit(body)
        return {'Circuit Req': {"measured_unit": "Ω",'resistance': result}}, 200

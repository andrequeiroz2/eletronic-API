from flask import Response, request, json
from flask_restful import Resource
from database.query_db import get_all_element, get_color
from calculations.resistor.resistor_calc import resistor_calc


#retorna a tabela de referencia de resistores
class ResistorApi(Resource):
    def get(self):
        resistor_result = get_all_element()
        resistor_dict = {}
        for i in resistor_result:
            resistor_dict[i.color] = {'value': i.value, 'factor': i.factor, 'tolerance': i.tolerance,
                                      'coefficient': i.coefficient, 'measured_unit': i.measured_unit}

        resistor_json = json.dumps(resistor_dict)
        return Response(resistor_json, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        result = resistor_calc(body)
        return {'Resistance': result}, 200


#retorna os valores de referencia por cor
class ResistorColorApi(Resource):
    def get(self, color):
        color_result = get_color(color)
        color_dict = {}
        color_dict[color_result.color] = {'value': color_result.value,
                                          'factor': color_result.factor,
                                          'tolerance': color_result.tolerance,
                                          'coefficient': color_result.coefficient,
                                          'measured_unit': color_result.measured_unit}

        color_json = json.dumps(color_dict)
        return Response(color_json, mimetype="application/json", status=200)

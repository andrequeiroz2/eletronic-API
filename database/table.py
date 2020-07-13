from.db import db
from .models import Resistor
from .query_db import get_count

colors = ["preto", "marrom", "vermelho", "laranja", "amarelo", "verde",
          "azul", "violeta", "cinza", "branco", "dourado", "prata"]

value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0]

factor = [1, 10, 100, 1000, 10000, 100000,
               1000000, 10000000, 0, 0, 0.1, 0.01]

tolerance = ["null", "+|- 1%", "+|- 2%", "null", "null",
             "+|- 0.5%", "+/- 0.25%", "+|- 0.1%",
             "+|- 0.05%", "null", "+|- 5%", "+|- 10%"]


measured_unit = ["\u03A9","\u03A9","\u03A9","K\u03A9","K\u03A9","K\u03A9","M\u03A9","M\u03A9","null","null","\u03A9","\u03A9"]

variable = [0, 0.01, 0.02, 0, 0, 0.005, 0.0025, 0.001, 0.0005, 0, 0.05, 0.1]

coefficient_temp = ["null", "100PPM|\u2103", "50PPM|\u2103", "15PPM|\u2103", "25PPM|\u2103",
                    "null", "10PPM|\u2103", "5PPM|\u2103", "null", "null", "null", "null"]


def create_table():
    db.create_all()
    print('Create Table: OK')


def populate_table():
    colors_len = len(colors)
    count = get_count()

    if count == 0:
        for i in range(colors_len):
            resistor = Resistor(color=colors[i], value=value[i], factor=factor[i],
                                tolerance=tolerance[i], measured_unit=measured_unit[i],
                                variable=variable[i], coefficient=coefficient_temp[i])
            db.session.add(resistor)
            db.session.commit()
    else:
        pass
    print('Populate Table: OK')
from database.models import Resistor


def resistor_calc(obj):
    color_list = []
    for x in obj.values():
        value = x
        color_list.append(value)

    color_len = (len(color_list))

    if color_len == 3:
        value_1 = Resistor.query.filter_by(color=color_list[0]).first()
        value_2 = Resistor.query.filter_by(color=color_list[1]).first()
        value_3 = Resistor.query.filter_by(color=color_list[2]).first()
        if (value_1.color == "dourado" or value_1.color == "prata") or\
            (value_2.color == "dourado" or value_2.color =="prata") or\
            (value_3.color == "cinza" or value_3.color =="branco"):
            return {"status": "error", "msg": "reference value does not exist"}
        resistance = ((value_1.value*10) + value_2.value) * value_3.factor
        unit = value_3.measured_unit
        variable = resistance * 0.2
        resistance_max = resistance + variable
        resistance_min = resistance - variable
        tolerance = "+/-20%"
        coef = "null"

    elif color_len == 4:
        value_1 = Resistor.query.filter_by(color=color_list[0]).first()
        value_2 = Resistor.query.filter_by(color=color_list[1]).first()
        value_3 = Resistor.query.filter_by(color=color_list[2]).first()
        value_4 = Resistor.query.filter_by(color=color_list[3]).first()
        if (value_1.color == 'dourado' or value_1.color == 'prata') or\
            (value_2.color == 'dourado' or value_2.color == 'prata') or\
            (value_3.color == 'cinza' or value_3.color == 'branco') or\
            (value_4.color == 'preto' or value_4.color == 'marron' or value_4.color == 'amarelo' or value_4.color == 'branco'):
            return {"status": "error", "msg": "reference value does not exist"}
        resistance = ((value_1.value*10) + value_2.value) * value_3.factor
        unit = value_3.measured_unit
        variable = resistance * value_4.variable
        resistance_max = resistance + variable
        resistance_min = resistance - variable
        tolerance = value_4.tolerance
        coef = "null"


    elif color_len == 5:
        value_1 = Resistor.query.filter_by(color=color_list[0]).first()
        value_2 = Resistor.query.filter_by(color=color_list[1]).first()
        value_3 = Resistor.query.filter_by(color=color_list[2]).first()
        value_4 = Resistor.query.filter_by(color=color_list[3]).first()
        value_5 = Resistor.query.filter_by(color=color_list[4]).first()
        if (value_1 == 'dourado' or value_1 == 'prata') or \
           (value_2 == 'dourado' or value_2 == 'prata') or \
           (value_3 == 'dourado' or value_3 == 'prata') or \
           (value_4 == 'cinza' or value_4 == 'branco') or \
           (value_5 == 'preto' or value_5 == 'marron' or value_5 == 'amarelo' or value_5 == 'branco'):
            return {"status": "error", "msg": "reference value does not exist"}
        resistance = ((value_1.value*100) + (value_2.value*10) + value_3.value) * value_4.factor
        unit = value_4.measured_unit
        variable = resistance * value_5.variable
        resistance_max = resistance + variable
        resistance_min = resistance - variable
        tolerance = value_5.tolerance
        coef = "null"


    elif color_len == 6:
        value_1 = Resistor.query.filter_by(color=color_list[0]).first()
        value_2 = Resistor.query.filter_by(color=color_list[1]).first()
        value_3 = Resistor.query.filter_by(color=color_list[2]).first()
        value_4 = Resistor.query.filter_by(color=color_list[3]).first()
        value_5 = Resistor.query.filter_by(color=color_list[4]).first()
        value_6 = Resistor.query.filter_by(color=color_list[5]).first()
        if (value_1.color == 'dourado' or value_1.color == 'prata') or \
           (value_2.color == 'dourado' or value_2.color == 'prata') or \
           (value_3.color == 'dourado' or value_3.color == 'prata') or \
           (value_4.color == 'cinza' or value_4.color == 'branco') or \
           (value_5.color == 'preto' or value_5.color == 'laranja' or value_5.color == 'amarelo' or value_5.color == 'branco') or \
           (value_6.color == 'preto' or value_6.color == 'verde' or value_6.color == 'cinza' or value_6.color == 'branco' or value_6.color == 'dourado' or value_6.color == 'prata'):
            return {"status": "error", "msg": "reference value does not exist"}
        resistance = ((value_1.value*100) + (value_2.value*10) + value_3.value) * value_4.factor
        unit = value_4.measured_unit
        variable = resistance * value_5.variable
        resistance_max = resistance + variable
        resistance_min = resistance - variable
        tolerance = value_5.tolerance
        coef = value_6.coefficient


    if resistance == 0:
        return {"status": "error", "msg": "reference value does not exist"}

    result = converter(resistance, unit, resistance_max, resistance_min)


    return {"measured_unit": unit, "resistance": result[0], "tolerance": tolerance,
            "resistance_max": result[1], "resistance_min": result[2],
            'coefficient': coef}


def converter(resistance, unit, max, min):

    if type(resistance) == float and unit == "\u03A9":
        if resistance <= 0:
            result = "{:.3f}".format(resistance)
        else:
            num = resistance
            rest = num % 1
            if rest == 0:
                result = str(int(resistance))
            else:
                result = "{:.3f}".format(resistance)
        if max <= 0:
            r_max = "{:.3f}".format(max)
        else:
            num = max
            rest = num % 1
            if rest == 0:
                r_max = str(int(max))
            else:
                r_max = "{:.3f}".format(max)
        if min <= 0:
            r_min = "{:.3f}".format(min)
        else:
            num = min
            rest = num % 1
            if rest == 0:
                r_min = str(int(min))
            else:
                r_min = "{:.3f}".format(min)
    else:
        if unit == "\u03A9":
            result = str(resistance)
            if type(max) == float:
                if max <= 0:
                    r_max = "{:.3f}".format(max)
                else:
                    num = max
                    rest = num % 1
                    if rest == 0:
                        r_max = str(int(max))
                    else:
                        r_max = "{:.3f}".format(max)
            if type(min) == float:
                if min <= 0:
                    r_min = "{:.3f}".format(min)
                else:
                    num = min
                    rest = num % 1
                    if rest == 0:
                        r_min = str(int(min))
                    else:
                        r_min = "{:.3f}".format(min)

    if type(resistance) == float and unit == "K\u03A9":
        result = "{:.3f}".format((resistance / 1000))
    else:
        if unit == "K\u03A9":
            result = str(int(resistance / 1000))
            if type(max) == float:
                if max <= 0:
                    r_max = "{:.3f}".format(max / 1000)
                else:
                    num = max
                    rest = num % 1
                    if rest == 0:
                        r_max = str(int(max / 1000))
                    else:
                        r_max = "{:.3f}".format(max / 1000)
            if type(min) == float:
                if min <= 0:
                    r_min = "{:.3f}".format(min / 1000)
                else:
                    num = min
                    rest = num % 1
                    if rest == 0:
                        r_min = str(int(min / 1000))
                    else:
                        r_min = "{:.3f}".format(min / 1000)

    if type(resistance) == float and unit == "M\u03A9":
        result = "{:.3f}".format((resistance / 1000000))
    else:
        if unit == "M\u03A9":
            result = str(int(resistance / 1000000))
            if type(max) == float:
                if max <= 0:
                    r_max = "{:.3f}".format(max / 1000000)
                else:
                    num = max
                    rest = num % 1
                    if rest == 0:
                        r_max = str(int(max / 1000000))
                    else:
                        r_max = "{:.3f}".format(max / 1000000)
            if type(min) == float:
                if min <= 0:
                    r_min = "{:.3f}".format(min / 1000000)
                else:
                    num = min
                    rest = num % 1
                    if rest == 0:
                        r_min = str(int(min / 1000000))
                    else:
                        r_min = "{:.3f}".format(min / 1000000)

    return (result, r_max, r_min)

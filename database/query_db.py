from .models import Resistor


def get_count():
    count = Resistor.query.count()
    return count


def get_all_element():
    elements = Resistor.query.all()
    return elements


def get_color(color):
    color = Resistor.query.filter_by(color=color).first()
    return color

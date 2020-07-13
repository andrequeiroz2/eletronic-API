from flask import Blueprint, send_file


help_resistor = Blueprint('help_resistor', __name__)

#help circuit
@help_resistor.route('/help-resistor')
def show_static_pdf():
    return send_file('resources/resistor/help/help-resistor.pdf', attachment_filename='resistor-help.pdf')
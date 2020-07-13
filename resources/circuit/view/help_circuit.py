from flask import Blueprint,send_file


help_circuit = Blueprint('help_circuit', __name__)

#help circuit
@help_circuit.route('/help-circuit')
def show_static_pdf():
    return send_file('resources/circuit/help/circuit-help.pdf', attachment_filename='circuit-help.pdf')
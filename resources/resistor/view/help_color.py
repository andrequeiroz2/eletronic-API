from flask import Blueprint, send_file


help_color = Blueprint('help_color', __name__)

#help color
@help_color.route('/help-color')
def show_static_pdf():
    return send_file('resources/resistor/help/help-color.pdf', attachment_filename='color-help.pdf')

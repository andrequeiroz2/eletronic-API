from flask import render_template, Blueprint
from database.query_db import get_all_element

table_resistor = Blueprint('table_resistor', __name__)

#view table of resistor
@table_resistor.route('/table')
def get_table():
    elements = get_all_element()
    return render_template('resistor.html', element=elements)

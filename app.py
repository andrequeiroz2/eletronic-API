import os
from flask import Flask
from database.db import initialize_db
from database.table import create_table, populate_table
from flask_restful import Api
from resources.routes import initialize_routes
from resources.resistor.view.table_resistor import table_resistor
from resources.circuit.view.help_circuit import help_circuit
from resources.resistor.view.help_resistor import help_resistor
from resources.resistor.view.help_color import help_color
from resources.index.view.index import index_view


app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = '6ce5c7642138041a9c4c6495b4525c8d'

basedir = os.path.abspath(os.path.dirname('database/'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'resistor.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


initialize_db(app)
initialize_routes(api)


with app.app_context():
    create_table()
    populate_table()

app.register_blueprint(table_resistor)
app.register_blueprint(help_circuit)
app.register_blueprint(help_resistor)
app.register_blueprint(help_color)
app.register_blueprint(index_view)

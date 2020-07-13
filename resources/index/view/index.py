from flask import Blueprint, render_template


index_view = Blueprint('index', __name__)


@index_view.route('/')
def index():
    return render_template('index.html')
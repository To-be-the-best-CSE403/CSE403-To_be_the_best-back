from flask import Blueprint

views = Blueprint('views', __name__)


@views.route('/home', methods=['GET'])
def api_home():
    return 'Hello, World!'

from flask import Blueprint, request
from werkzeug.datastructures import CombinedMultiDict, MultiDict
from tools.CORS import crossdomain
from tools.Toolkit import respond
from view import list_cars, add_car, car_info

cars_api = Blueprint('cars', __name__, url_prefix='/cars')

@cars_api.route('/', methods=['GET'])
@crossdomain(origin='*')
def get_cars():
	parameters = CombinedMultiDict([request.args, request.form])
	response = list_cars(parameters)
	return respond(response)

@cars_api.route('/add', methods=['POST'])
@crossdomain(origin='*')
def save_car():
	parameters = request.get_json()
	response = add_car(parameters)
	return respond(response)

@cars_api.route('/car_info/', methods=['GET'])
@crossdomain(origin='*')
def get_car():
	parameters = CombinedMultiDict([request.args, request.form])
	response = car_info(parameters)
	return respond(response)

@cars_api.route('/delete_location', methods=['GET'])
@crossdomain(origin='*')
def delete_user_state():
	parameters = CombinedMultiDict([request.args, request.form])
	response = delete_user_location(parameters)
	return respond(response)

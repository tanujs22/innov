from flask import Blueprint, request
from werkzeug.datastructures import CombinedMultiDict, MultiDict
from tools.CORS import crossdomain
from tools.Toolkit import respond
from view import list_cars, add_car, car_info, sell_car, rent_car, rent_revoke

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

@cars_api.route('/sell/', methods=['POST'])
@crossdomain(origin='*')
def sell():
	parameters = request.get_json()
	response = sell_car(parameters)
	return respond(response)

@cars_api.route('/rent/', methods=['POST'])
@crossdomain(origin='*')
def rent():
	parameters = request.get_json()
	response = rent_car(parameters)
	return respond(response)

@cars_api.route('/revoke/', methods=['POST'])
@crossdomain(origin='*')
def revoke():
	parameters = request.get_json()
	response = rent_revoke(parameters)
	return respond(response)

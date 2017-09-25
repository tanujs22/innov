from model import Car

def list_cars(parameters):
    response = {"data": [], "status": "failed"}
    list_type = parameters.get('list_type', None)
    lc = Car()
    if list_type:
        try:
            result = lc.fetch_all(list_type)
            response['data'] = result
            response['status'] = 'success'
        except:
            response
    try:
        result = lc.fetch_all(list_type)
        response['data'] = result
        response['status'] = 'success'
    except:
        return response
    return response

def car_info(parameters):
    response = {"data": [], "status": "failed"}
    car_id = parameters['id']
    lc = Car()
    try:
        result = lc.fetch_one(car_id)
        if result['car_for'] == 'rent':
            res = lc.fetch_rent(car_id)
            response['rent_info'] = res['rent_data']
        response['data'] = result
        response['status'] = 'success'
    except:
        return response
    return response


def add_car(parameters):
    response = {"message": [], "status": "failed"}
    try:
        manufacturer = parameters['manufacturer']
        model = parameters['model']
        color = parameters['color']
        yob = parameters['yob']
        rto_reg = parameters['rto']
        fuel_type = parameters['fuel']
        cost_price = parameters['cost_price']
        selling_price = parameters.get('selling_price', None)
        status = parameters.get('status', None)
        car_for = parameters.get('car_for','sale')
    except KeyError, e:
        print e
        response['message'] = 'Please provide all the information.'
        return response
    try:
        ac = Car()
        result = ac.save_car(manufacturer, model, color, yob, rto_reg, fuel_type, cost_price, selling_price, car_for, status)
        print result
        if 'success' in result:
            print 'got in result suc'
            response['message'] = 'Car saved as ' + result['success']
            response['status'] = "success"
            return response
        else:
            response['message'] = result['error']
            return response
    except:
        return response
    
def sell_car(parameters):
    response = {"message": [], "status": "failed"}
    dt = car_info(parameters)
    try:
        car_id = dt['data']['_id']
    except:
        response['message'] = 'Wrong car id'
    selling_price = parameters['amount']
    sl = Car()
    if dt['data']['status'] == '':
        sl.sl_car(car_id, selling_price)
        response['message'] = 'Car Sold'
        response['status'] = 'success'
        return response
    else:
        response['message'] = 'This car has been either sold or has been rented.'
        return response

def rent_car(parameters):
    response = {"message": [], "status": "failed"}
    dt = car_info(parameters)
    try:
        car_id = dt['data']['_id']
        origin = parameters['origin']
        destination = parameters['destination']
    except:
        response['message'] = 'Wrong car id'
        return response
    rent = parameters['amount']
    sr = Car()
    if (dt['data']['status'] == ''):
        sr.rt_car(car_id, rent, origin, destination)
        response['message'] = 'The car has been booked.'
        response['status'] = 'success'
    else: 
        response['message'] = 'This car has been either sold or has been rented.'
    return response

def rent_revoke(parameters):
    response = {"message": [], "status": "failed"}
    dt = car_info(parameters)
    try:
        car_id = dt['data']['_id']
    except:
        response
    sr = Car()
    if (dt['data']['status'] == 'rented'):
        result = sr.revoke(car_id)
        if result:
            response['message'] = 'The car is available now!'
            response['status'] = 'success'
            return response
    else: 
        response['message'] = 'The car was already available!'
    return response

def sale_profit(parameters):
    response = {"message": [], "status": "failed"}
    sp = Car()
    try:
        sp.cal_sale_prof()
        return 'x'
    except:
        return response

from model import Car

def list_cars(parameters):
    response = {"data": [], "status": "failed"}
    list_type = parameters.get('list_type', None)
    lc = Car()
    if list_type:
        try:
            result = lc.fetch_all(list_type)
            print result
            response['data'] = result
            response['status'] = 'success'
        except:
            response
    try:
        result = lc.fetch_all(list_type)
        print result
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
    

# def car_info(parameters):
#     response = {"message": [], "status": "failed"}
    
#     return response





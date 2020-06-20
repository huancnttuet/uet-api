from flask_restplus import Namespace, Resource, reqparse
from app.services import device as service
from flask import request
api = Namespace('device', description='Device id')


parser = reqparse.RequestParser()
parser.add_argument('device_name')
parser.add_argument('device_id')


@api.route('')
class Kiki(Resource):

    def post(seft):
        print(request.get_json())
        req = request.get_json()
        d_id = req['device_id']
        d_name = req['device_name']
        service.add_device(d_id, d_name)
        return {'status': 200}


@api.route('/get-add-device-id')
class Hihi(Resource):
    def get(self):

        return service.get_all_device_id()

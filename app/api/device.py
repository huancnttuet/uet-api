from flask_restplus import Namespace, Resource, reqparse
from app.services import device as service
from flask import request
api = Namespace('device', description='Device id')


parser = reqparse.RequestParser()
parser.add_argument('device_name')
parser.add_argument('device_id')


@api.route('/')
class Kiki(Resource):
    def get(self):

        return 'kiki'

    @api.expect(parser)
    def post(seft):

        args = parser.parse_args()
        d_name = args['device_name']
        d_id = args['device_id']
        service.add_device(d_name, d_id)
        return "ok"


@api.route('/get-add-device-id')
class Hihi(Resource):
    def get(self):

        return service.get_all_device_id()

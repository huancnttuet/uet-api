from flask_restplus import Namespace, Resource, reqparse
from app.services import device as service
from app.services import fcm_notify as service2
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
        service2.send_notify_single(
            d_id, "Nhận thông báo", "Bạn vừa đăng ký nhận thông báo thành công")
        return {'status': 200}


@api.route('/delete')
class Haha(Resource):

    def post(seft):
        req = request.get_json()
        d_id = req['device_id']
        service.delete_device(d_id)
        return {'status': 200}


@api.route('/get-add-device-id')
class Hihi(Resource):
    def get(self):

        return service.get_all_device_id()

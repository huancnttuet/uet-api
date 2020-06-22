from flask_restplus import Namespace, Resource, reqparse
from app.services import fcm_notify as service
from flask import request
api = Namespace('notify', description='Thông báo')


parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('message')
parser.add_argument('action')
parser.add_argument('payload')


@api.route('/sendall')
class Kiki(Resource):
    @api.expect(parser)
    def get(seft):
        args = parser.parse_args()
        service.send_notify(args.title, args.message,
                            args.action, args.payload)
        return "ok"


parser1 = reqparse.RequestParser()
parser1.add_argument('divice_id')
parser1.add_argument('title')
parser1.add_argument('message')
parser1.add_argument('action')
parser1.add_argument('payload')


@api.route('/sendone')
class Kiiki(Resource):
    @api.expect(parser)
    def get(seft):
        args = parser.parse_args()
        service.send_notify_single(args.device_id, args.title, args.message,
                                   args.action, args.payload)
        return "ok"

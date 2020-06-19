from flask_restplus import Namespace, Resource, reqparse
from app.services import fcm_notify as service
from flask import request
api = Namespace('notify', description='Thông báo')


parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('message')


@api.route('')
class Kiki(Resource):
    @api.expect(parser)
    def get(seft):
        args = parser.parse_args()
        service.send_notify(args.title, args.message)
        return "ok"

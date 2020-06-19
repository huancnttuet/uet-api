from flask_restplus import Namespace, Resource, reqparse
from app.services import cron_job as service
from flask import request
api = Namespace('cronjob', description='Schedule jobs')


parser = reqparse.RequestParser()
parser.add_argument('status')


@api.route('')
class Kiki(Resource):
    @api.expect(parser)
    def get(seft):
        args = parser.parse_args()
        status = args.status
        if status == 'start' or status == '1':
            service.start_job()
            return "job running"
        if status == 'stop' or status == '0':
            service.stop_job()
            return "job stopped"
        return "not ok"

from flask_restplus import Namespace, Resource, reqparse
from app.services import import_data as service
from flask import request
api = Namespace('import', description='Device id')


@api.route('')
class Kiki(Resource):

    def get(seft):
        service.import_csv()
        return {'status': 200}

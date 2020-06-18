from flask_restplus import Namespace, Resource

api = Namespace('kiki', description='mokiki')


@api.route('/')
class Kiki(Resource):
    def get(self):
        return 'kiki'
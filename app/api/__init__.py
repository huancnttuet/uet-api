from flask_restplus import Api
from .test import api as kiki_ns


def init_app(app):
    api = Api(app,
              version='1.0',
              title='UETPLUS API',
              description='a mircro services')

    api.add_namespace(kiki_ns)

    return app

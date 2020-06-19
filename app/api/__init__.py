from flask_restplus import Api
from .device import api as kiki_ns
from .notify import api as notify_ns

def init_app(app):
    api = Api(app,
              version='1.0',
              title='UETPLUS API',
              description='a mircro services')

    api.add_namespace(kiki_ns)
    api.add_namespace(notify_ns)
    return app

from flask import Flask
from app import api
from werkzeug.contrib.fixers import ProxyFix


def create_app():
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    api.init_app(app)

    return app

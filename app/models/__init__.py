from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate(db=db)


def init_app(app):
    db.init_app(app)
    migrate.init_app(app)


from .device import DeviceModel
from .examtime import ExamtimeModel
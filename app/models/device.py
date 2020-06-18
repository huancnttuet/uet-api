from app.models import db


class DeviceModel(db.Model):
    __tablename__ = 'Devices'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    code = db.Column(db.String(128))

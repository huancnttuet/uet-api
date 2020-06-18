from app.models import db, DeviceModel


def add_device(device_id, device_name):
    newDevice = DeviceModel(name=device_name, code=device_id)
    db.session.add(newDevice)
    db.session.commit()


def get_all_device_id():
    divices = DeviceModel.query.all()
    r = []
    for d in divices:
        r.append(d.code)
    return r

from app.models import db


class ExamtimeModel(db.Model):
    __tablename__ = 'examtimes'

    id = db.Column(db.Integer, primary_key=True)
    hour = db.Column(db.String(128))
    day_of_week = db.Column(db.String(256))
    date = db.Column(db.String(256))
    subject_code = db.Column(db.String(256))
    subject_name = db.Column(db.String(256))
    credits = db.Column(db.String(256))
    teacher = db.Column(db.String(256))
    student_total = db.Column(db.String(256))
    pt = db.Column(db.String(256))
    ct = db.Column(db.String(256))
    room = db.Column(db.String(256))
    note = db.Column(db.String(256))

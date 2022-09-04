from application import db

class scored(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.String(5), default=False, nullable=False)
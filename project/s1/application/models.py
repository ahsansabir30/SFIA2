from application import db

class FootballStadiums(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(30), unique=True, nullable=False)
    stadium = db.Column(db.String(30), unique=True, nullable=False)
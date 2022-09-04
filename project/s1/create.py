from application import db
from application.models import scored

db.drop_all()
db.create_all()
db.session.commit()
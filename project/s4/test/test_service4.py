from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import FootballStadiums

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
            DEBUG=True,
            WTF_CSRF_ENABLED=False,
            SECRET_KEY = 'NADSKJADSNJDA54DSAJKNDAJ4'
        )
        return app

    def setUp(self):
        db.create_all()
        stadium = FootballStadiums(team="Manchester United", stadium="Old Trafford")
        db.session.add(stadium)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponseService4(TestBase):
    def test_correct_stadium_team(self):
        response = self.client.post(url_for('outcome'), json={'team':'Manchester United', 'stadium':'Old Trafford'})
        self.assertIn(b'True', response.data)

    def test_incorrect_stadium_team(self):
        response = self.client.post(url_for('outcome'), json={'team':'Manchester United', 'stadium':'Trafford'})
        self.assertIn(b'False', response.data)
    
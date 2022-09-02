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

class TestResponseService2(TestBase):
    def test_page_response(self):
        response = self.client.get(url_for('getstadium'))
        self.assert200(response)
        assert response.data.decode('utf-8') == "Old Trafford"
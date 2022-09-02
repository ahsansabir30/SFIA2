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
        # creating test object in the database
        db.create_all()
        # creating a fake plan
        team = FootballStadiums(team="Liverpool", stadium="Anfield")
        db.session.add(team)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponseService2(TestBase):
    def test_page_response(self):
        response = self.client.get(url_for('getteams'))
        self.assert200(response)
        assert response.data.decode('utf-8') == "Liverpool"
from flask import url_for
from flask_testing import TestCase
import requests_mock
from application import app, db
from application.models import scored

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
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponseServiceOne(TestBase):
    def test_home_page(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'THE FOOTBALL GENERATOR', response.data)
        
    def test_correct_team_stadium(self):
        with requests_mock.Mocker() as m:
            m.get('http://s2:5001/get/teams', text='Bayern Munich')
            m.get('http://s3:5002/get/stadiums', text='Allianz Arena')
            m.post('http://s4:5003/outcome', text='True')
            
            response = self.client.get(url_for('football'))
            self.assertIn(b'YOU SCORED', response.data)
            assert scored.query.filter_by(score='score').first() is not None

    def test_incorrect_team_stadium(self):
        with requests_mock.Mocker() as m:
            m.get('http://s2:5001/get/teams', text='Bayern Munich')
            m.get('http://s3:5002/get/stadiums', text='Signal Iduna Park')
            m.post('http://s4:5003/outcome', text='False')

            response = self.client.get(url_for('football'))
            self.assertIn(b'YOU MISSED', response.data)
            assert scored.query.filter_by(score='miss').first() is not None
            
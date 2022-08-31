from flask import url_for
from flask_testing import TestCase
import requests_mock
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponseServiceOne(TestBase):
    def test_correct_team_stadium(self):
        with requests_mock.Mocker() as m:
            m.get('http://s2:5001/get/teams', text='Liverpool')
            m.get('http://s3:5002/get/stadiums', text='Anfield')
            m.post('http://s4:5003/outcome', text='True')
            
            response = self.client.get(url_for('football'))
            self.assertIn(b'YOU SCORED', response.data)

    def test_incorrect_team_stadium(self):
        with requests_mock.Mocker() as m:
            m.get('http://s2:5001/get/teams', text='Arsenal')
            m.get('http://s3:5002/get/stadiums', text='Old Trafford')
            m.post('http://s4:5003/outcome', text='False')

            response = self.client.get(url_for('football'))
            self.assertIn(b'YOU MISSED', response.data)
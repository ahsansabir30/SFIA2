from application import app
from flask import render_template
import requests

@app.route('/football', methods=['POST', 'GET'])
def football():
    team = requests.get('http://s2:5001/get/teams').text
    stadium = requests.get('http://s3:5002/get/stadiums').text
    response = {
        'team': team,
        'stadium': stadium
    }
    outcome = requests.post('http://s4:5003/outcome', json=response).text
    return render_template('generator.html', team=team, stadium=stadium, outcome=outcome)

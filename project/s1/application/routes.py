from application import app, db
from flask import render_template
import requests
from application.models import scored

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/football', methods=['POST', 'GET'])
def football():
    team = requests.get('http://s2:5001/get/teams').text
    stadium = requests.get('http://s3:5002/get/stadiums').text
    response = {
        'team': team,
        'stadium': stadium
    }
    outcome = requests.post('http://s4:5003/outcome', json=response).text
    
    if str(outcome) == 'True':
        score = scored(score='score')
        db.session.add(score)
        db.session.commit()
    else:
        score = scored(score='miss')
        db.session.add(score)
        db.session.commit()

    tally = scored.query.filter_by(score='score').count()

    return render_template('generator.html', team=team, stadium=stadium, outcome=outcome, tally=tally)
    
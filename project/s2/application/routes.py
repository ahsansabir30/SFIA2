from flask import Response
from application import app
import random

@app.route('/get/teams', methods=['GET'])
def getteams():
    teams = [
        'Liverpool', 'Chelsea', 'Manchester United', 'Manchester City', 'Tottenham', 'Arsenal'
    ]
    random_team = random.choice(teams)
    return Response(random_team, mimetype='text/plain') 
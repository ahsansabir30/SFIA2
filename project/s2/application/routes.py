from flask import Response
from application import app
import random

@app.route('/get/teams', methods=['GET'])
def getteams():
    count_teams = FootballStadiums.query.count() 
    random_choice = random.randint(1, count_teams)
    random_team = FootballStadiums.query.get(random_choice).team
    return Response(random_team, mimetype='text/plain') 
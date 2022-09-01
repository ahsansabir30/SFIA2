from flask import Response, request
from application import app
from application.models import FootballStadiums
import json

@app.route('/outcome', methods=['GET', 'POST'])
def outcome():
    data = json.loads(request.data.decode('utf-8')) 
    team = data['team']
    team_stadium = FootballStadiums.query.filter_by(team='Liverpool').first().stadium

    if team_stadium ==  data['stadium']:
        outcome = str(True)
    else:
        outcome = str(False)
    return Response(outcome, mimetype='text/plain') 



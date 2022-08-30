from flask import Response, request
from application import app
import json

@app.route('/outcome', methods=['GET', 'POST'])
def outcome():
    teams = {
        'Liverpool':'Anfield', 
        'Chelsea':'Stamford Bridge', 
        'Manchester United':'Old Trafford', 
        'Manchester City':'Etihad', 
        'Tottenham':'Tottenham Hotspur', 
        'Arsenal':'Emirates'
    }
    
    data = json.loads(request.data.decode('utf-8')) 
    
    if teams.get(data['team']) ==  data['stadium']:
        outcome = str(True)
    else:
        outcome = str(False)

    return Response(outcome, mimetype='text/plain') 

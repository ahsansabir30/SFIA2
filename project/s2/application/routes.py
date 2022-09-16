from flask import Response
from application import app
import random

@app.route('/get/teams', methods=['GET'])
def getteams():
    teams = [
        'Bayern Munich', 'Borussia Dortmund', 'VfL Wolfsburg', 'Leverkusen', 'Eintracht Frankfurt', 'Borussia Mönchengladbach'
    ]
    random_team = random.choice(teams)
    return Response(random_team, mimetype='text/plain') 
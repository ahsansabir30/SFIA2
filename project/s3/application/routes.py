from flask import Response
from application import app
import random

@app.route('/get/stadiums', methods=['GET'])
def getstadium():
    count_stadiums = FootballStadiums.query.count() 
    random_choice = random.randint(1, count_stadiums)
    random_stadium = FootballStadiums.query.get(random_choice).stadium
    return Response(random_stadium, mimetype='text/plain') 
from flask import Response
from application import app
import random

@app.route('/get/stadiums', methods=['GET'])
def getstadium():
    stadiums = [
        'Allianz Arena', 'Signal Iduna Park', 'Volkswagen Arena', 'BayArena', 'Deutsche Bank Park', 'BORUSSIA-PARK'
    ]
    random_stadium = random.choice(stadiums)
    return Response(random_stadium, mimetype='text/plain') 
from application import db
from application.models import FootballStadiums

db.drop_all()
db.create_all()

teams = [
    {'Liverpool': 'Anfield'},
    {'Chelsea': 'Stamford Bridge'},
    {'Manchester United': 'Old Trafford'},
    {'Manchester City': 'Etihad'},
    {'Tottenham': 'Tottenham Hotspur'},
    {'Arsenal': 'Emirates'},
]

for team_dict in teams:
    for team, stadium in team_dict.items():
        add_team = FootballStadiums(team=team, stadium=stadium )
        db.session.add(add_team)
        db.session.commit()



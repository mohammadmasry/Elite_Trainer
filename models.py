from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PlayerProfile(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(80), nullable=False)
   age = db.Column(db.Integer, nullable=False)
   player_number = db.Column(db.Integer, nullable=False)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    attendees = db.Column(db.JSON, nullable=True)   


class Lineup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(10), nullable=False)  
    player_id = db.Column(db.Integer, nullable=False)   
    match_id = db.Column(db.Integer, nullable=True)   
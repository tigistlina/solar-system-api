from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    parent_planet = db.Column(db.String)
    habitable = db.Column(db.Boolean)
    gravity = db.Column(db.String)
    nickname = db.Column(db.String)

from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    habitable = db.Column(db.Boolean)
    gravity = db.Column(db.String)
    nickname = db.Column(db.String, nullable=True)
    moon_id = db.Column(db.Integer, db.ForeignKey("moon.id"))
    moon = db.relationship("Moon", back_populates="planets")

    def to_dict(self):
        return dict(
            name=self.name,
            description=self.description,
            size=self.size,
            habitable=self.habitable,
            id=self.id,
            gravity=self.gravity,
            nickname=self.nickname,
            moon_id = self.moon_id
            )

    @classmethod
    def from_dict(cls, planet_data):
        return  cls(
            name = planet_data["name"],
            description = planet_data["description"],
            size = planet_data["size"],
            habitable = planet_data["habitable"],
            gravity = planet_data["gravity"],
            nickname = planet_data["nickname"]
        )

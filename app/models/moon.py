from app import db

class Moon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    size = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    mass = db.Column(db.String, nullable=False)
    planets = db.relationship("Planet", back_populates="moon")


    def to_dict(self):
        return dict(
            description=self.description,
            size=self.size,
            id=self.id,
            mass=self.mass
            )

    @classmethod
    def from_dict(cls, moon_data):
        return  cls(
            mass = moon_data["mass"],
            description = moon_data["description"],
            size = moon_data["size"]

        )

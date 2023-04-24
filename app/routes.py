from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, size):
        self.id = id
        self.name = name
        self.description = description
        self.size = size

    def create_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            size=self.size
        )

planets = [
    Planet(1, "Earth", "habitable", "12742km in diameter"),
    Planet(2, "Mercury", "inhabitable", "4880km in diameter"),
    Planet(3, "Venus", "inhabitable", "12104km in diameter"),
    Planet(4, "Mars", "inhabitable", "6779km in diameter"),
    Planet(5, "Jupiter", "inhabitable", "139822km in diameter"),
    Planet(6, "Saturn", "inhabitable", "116460km in diameter")
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id=int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message": f"planet {planet_id} not found"}, 404))


@planets_bp.route("", methods=["GET"])
def get_list_of_planets():
    results =[]
    for planet in planets:
        results.append(planet.create_dict())
    return jsonify(results)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
        planet = validate_planet(planet_id)
        return planet.create_dict()



    
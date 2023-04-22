from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, size):
        self.id = id
        self.name = name
        self.description = description
        self.size = size

planets = [
    Planet(1, "Earth", "habitable", "12742km in diameter"),
    Planet(2, "Mercury", "inhabitable", "4880km in diameter"),
    Planet(3, "Venus", "inhabitable", "12104km in diameter"),
    Planet(4, "Mars", "inhabitable", "6779km in diameter"),
    Planet(5, "Jupiter", "inhabitable", "139822km in diameter"),
    Planet(6, "Saturn", "inhabitable", "116460km in diameter")
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
@planets_bp.route("", methods=["GET"])
def get_list_of_planets():
    results =[]
    for planet in planets:
        results.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            size=planet.size
        ))
    return jsonify(results)


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
@planets_bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
    try:
        planet_id=int(planet_id)
    except:
        return {"message": f"planet {planet_id} invalid"}, 400
    for planet in planets:
        if planet.id == planet_id:
            return dict(
                id=planet.id,
                name=planet.name,
                description=planet.description,
                size=planet.size
            )
        
    return {"message": f"planet {planet_id} not found"}, 404


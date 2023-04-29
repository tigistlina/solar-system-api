from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def handle_planet():
    request_body = request.get_json()
    new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            size=request_body["size"],
            parent_planet =request_body["parent_planet"],
            habitable =request_body["habitable"],
            gravity =request_body["gravity"],
            nickname =request_body["name"],
    )


    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)









# from flask import Blueprint, jsonify, abort, make_response

# class Planet:
#     def __init__(self, id, name, description, size, parent_planet, habitable, gravity, nickname):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.size = size
#         self.parent_planet = parent_planet
#         self.habitable = habitable
#         self.gravity = gravity
#         self.nickname = nickname

#     def create_dict(self):
#         return dict(
#             id=self.id,
#             name=self.name,
#             description=self.description,
#             size=self.size,
#             parent_planet = self.parent_planet,
#             habitable = self.habitable,
#             gravity = self.gravity,
#             nickname = self.nickname

#         )






# planets = [
#     Planet(1, "Earth", "habitable", "12742km in diameter"),
#     Planet(2, "Mercury", "inhabitable", "4880km in diameter"),
#     Planet(3, "Venus", "inhabitable", "12104km in diameter"),
#     Planet(4, "Mars", "inhabitable", "6779km in diameter"),
#     Planet(5, "Jupiter", "inhabitable", "139822km in diameter"),
#     Planet(6, "Saturn", "inhabitable", "116460km in diameter")
# ]


# def validate_planet(planet_id):
#     try:
#         planet_id=int(planet_id)
#     except:
#         abort(make_response({"message": f"planet {planet_id} invalid"}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     abort(make_response({"message": f"planet {planet_id} not found"}, 404))


# @planets_bp.route("", methods=["GET"])
# def get_list_of_planets():
#     results =[]
#     for planet in planets:
#         results.append(planet.create_dict())
#     return jsonify(results)

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def get_planet(planet_id):
#         planet = validate_planet(planet_id)
#         return planet.create_dict()

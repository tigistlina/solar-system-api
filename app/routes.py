from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request , abort

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message": f"Planet {planet_id} not found"}, 404))

    return planet

@planets_bp.route("", methods=["POST"])
def handle_planet():
    request_body = request.get_json()
    new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            size=request_body["size"],
            moon_of_planet =request_body["moon_of_planet"],
            habitable =request_body["habitable"],
            gravity =request_body["gravity"],
            nickname =request_body["name"],
    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all()
    results = []
    for planet in planets:
        results.append(
            dict(
                id =planet.id,
                name=planet.name,
                description=planet.description,
                size=planet.size,
                moon_of_planet =planet.moon_of_planet,
                habitable =planet.habitable,
                gravity =planet.gravity,
                nickname =planet.nickname
            )
        )

    return jsonify(results)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return {

            "id" : planet.id,
            "name" :planet.name,
            "description" : planet.description,
            "size" : planet.size,
            "moon_of_planet" : planet.moon_of_planet,
            "habitable" : planet.habitable,
            "gravity" :planet.gravity,
            "nickname" : planet.nickname

            }
@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet_to_update= validate_planet(planet_id)
    planet_data= request.get_json()

    planet_to_update.name = planet_data["name"]
    planet_to_update.description = planet_data["description"]
    planet_to_update.size= planet_data["size"]
    planet_to_update.moon_of_planet = planet_data["moon_of_planet"]
    planet_to_update.habitable = planet_data["habitable"]
    planet_to_update.gravity = planet_data["gravity"]
    planet_to_update.nickname = planet_data["nickname"]
    
    db.session.commit()

    return make_response(f"Planet { planet_to_update.name} updated", 200)

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet_to_delete = validate_planet(planet_id)

    db.session.delete(planet_to_delete)
    db.session.commit()

    return make_response(f"Planet {planet_to_delete.name} successfully deleted", 200)




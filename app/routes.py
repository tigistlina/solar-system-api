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
                parent_planet =planet.parent_planet,
                habitable =planet.habitable,
                gravity =planet.gravity,
                nickname =planet.nickname
            )
        )

    return jsonify(results)


from app import db
from app.models.moon import Moon
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request , abort
from .helpers import validate_model

moons_bp = Blueprint("moons_bp", __name__, url_prefix="/moons")

@moons_bp.route("", methods=["POST"])
def create_moon():
    request_body = request.get_json()
    try:
        new_moon = Moon.from_dict(request_body)

        db.session.add(new_moon)
        db.session.commit()
        return make_response(jsonify(f"Moon {new_moon.id} successfully created"), 201)
    except KeyError as e:
        abort(make_response({"message": f"missing required value: {e}"}, 400))

@moons_bp.route("", methods=["GET"])
def read_all_moons():
    moons = Moon.query.all()

    moons_response = [moon.to_dict() for moon in moons]

    return jsonify(moons_response)

@moons_bp.route("<moon_id>/planets", methods=["POST"])
def create_planet(moon_id):
    moon = validate_model(Moon, moon_id)
    request_body = request.get_json()
    try:
        new_planet = Planet.from_dict(request_body)
        new_planet.moon = moon

        db.session.add(new_planet)
        db.session.commit()

        return make_response(jsonify(f"Planet {new_planet.name} has moon {moon.id} successfully created"), 201)
    except KeyError as e:
        abort(make_response({"message": f"missing required value: {e}"}, 400))

@moons_bp.route("<moon_id>/planets", methods=["GET"])
def read_planets(moon_id):
    moon = validate_model(Moon, moon_id)

    planets_response = []
    for planet in moon.planets:
        planets_response.append(planet.to_dict())

    return(jsonify(planets_response))

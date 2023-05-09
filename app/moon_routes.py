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

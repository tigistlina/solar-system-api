import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_planet(app):
    planet = Planet(
        description="A dusty, cold, desert world with a very thin atmosphere",
        gravity="3.721 m/s²",
        habitable=False,
        moon_of_planet="Phobos & Deimos",
        name="Mars",
        nickname="Mars",
        size="6,792 km"
    )
    db.session.add(planet)
    db.session.commit()
    return planet
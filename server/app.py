# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

@app.route('/earthquakes/<int:id>')
def get_earthquake_by_id(id):
    """
    Return earthquake data by its ID.
    If not found, return JSON error with status 404.
    """
    # Query the earthquake by id
    quake = Earthquake.query.filter_by(id=id).first()

    # If not found, return 404 JSON response
    if not quake:
        body = {"message": f"Earthquake {id} not found."}
        return make_response(body, 404)

    # If found, return JSON with earthquake details
    body = {
        "id": quake.id,
        "magnitude": quake.magnitude,
        "location": quake.location,
        "year": quake.year
    }

    return make_response(body, 200)

@app.route('/earthquakes/magnitude/<float:magnitude>')
def get_earthquakes_by_magnitude(magnitude):
    """
    Return all earthquakes with magnitude >= given value.
    Response includes count and list of matching earthquakes.
    """

    # Query all matching earthquakes
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    # Build list of quake dictionaries
    quakes_list = [
        {
            "id": q.id,
            "magnitude": q.magnitude,
            "location": q.location,
            "year": q.year
        }
        for q in quakes
    ]

    # JSON body includes count and list
    body = {
        "count": len(quakes_list),
        "quakes": quakes_list
    }

    return make_response(body, 200)


if __name__ == '__main__':
    app.run(port=5555, debug=True)

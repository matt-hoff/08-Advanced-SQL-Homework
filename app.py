from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
#declare column types
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import desc
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(engine, reflect=True)

# Assign the demographics class to a variable called `Demographics`
Measurement = Base.classes.measurement
Station = Base.classes.station

Session = Session(engine)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to the Weather API!<br/>"
    )

############################

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data as json"""
    query_prcp = Session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= '2016-08-23').all()
    return jsonify(query_prcp)

############################

@app.route("/api/v1.0/stations")
def station():
    """Return the station data as json"""
    query_stations = Session.query(Station.station).all()
    return jsonify(query_stations)

# ##############################

@app.route("/api/v1.0/tobs")
def tobs():
    """Return the tempurature data as json"""
    query_tobs = Session.query(Measurement.tobs).\
    filter(Measurement.date >= '2016-08-23').all()
    return jsonify(query_tobs)

##################################
# #I commented out the below as it was causing syntax errors and the above end paths were working. I did not want the below to effect the above from being run. I will review the solution for how to set up these queries and route
# @app.route("/api/v1.0/<start>")
# def start_tempuratures():
#     """Fetch the min, avg, and max tempuratures for a selected date."""
#     results = Session.query(func.min(Measurement.tobs).all()
#     start = '2016-08-23'
#     for date in results:
#         query_start = date > start

#         if search_term == start:
#             return jsonify()

#     return jsonify({"error": f"tempurture not found."}), 404

# ####################################

# @app.route("/api/v1.0/<start>/<end>")
# def start_end_tempuratures():
#     """Fetch the min, avg, and max tempuratures for a selected date."""

#     end = '2017-08-23'
#     for date in justice_league_members:
#         query_start = date > start

#         if search_term == end:
#             return jsonify()

#     return jsonify({"error": f"tempurture not found."}), 404

if __name__ == "__main__":
    app.run(debug=True)
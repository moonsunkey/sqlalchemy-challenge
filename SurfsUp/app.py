# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,func
from sqlalchemy.engine import reflection
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine,reflect=True)

# reflect the tables
measurement = Base.classes.measurement
station = Base.classes.station

# Save references to each table

tables = {}
for class_name in Base.classes.keys():
    table_reference = getattr(Base.classes, class_name)
    tables[measurement] = table_reference
    tables[station] = table_reference

# Create our session (link) from Python to the DB

session = Session(engine)

#Calculate the date one year before the most recent data in the database first

most_recent_date = session.query(func.max(measurement.date)).scalar()
one_year_before = dt.datetime.strptime(most_recent_date,'%Y-%m-%d').date() - dt.timedelta(365)

session.close()
#################################################

# Flask Setup

from flask import Flask, jsonify

app = Flask(__name__)

#################################################
# Flask Routes

# Define the available routes to return on the landing page 
@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs"
    )
# The precipitation route: 

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results=session.query(measurement.date,measurement.prcp).\
    filter(measurement.date>=one_year_before).all()

    session.close()

#Define precipation_data as a dictionary

    precipitation_data = {date: prcp for date, prcp in results}

#To return the jsonified precipitation data for the last year in the database 
    return jsonify(precipitation_data)

# Stations route:
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results=session.query(station.station).all()
    session.close()

#Define stations_data as a list

    stations_data = [station[0] for station in results]

# To return jsonified data of all of the stations in the database (3 points)
    return jsonify(stations_data)

# tobs route:
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    results=session.query(measurement.date,measurement.tobs).\
    filter(measurement.date>=one_year_before, measurement.station == 'USC00519281').all()
    session.close()
#results filtered to the most active station
    
#define tobs_data as a dictionary
    tobs_data = {date: tobs for date, tobs in results}

#To return the jsonified data for the last year of data (3 points)
    return jsonify(tobs_data)


#Start Route 

#Define route using 'start' as a variable 
@app.route('/api/v1.0/<start>', methods=['GET'], endpoint='start_only')
def start(start):
    session = Session(engine)
    # Ensuring that the session is closed after the operation
    try:
        # Querying min, max, and avg temperatures from the start date to the end of the dataset
        results = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
                          filter(measurement.date >= start).all()

        # Unpacking the result tuple
        min_temp, max_temp, avg_temp = results[0]
        return jsonify({
            "Minimum Temperature": min_temp, 
            "Maximum Temperature": max_temp, 
            "Average Temperature": avg_temp
        })
    finally:
        session.close()

#Start and end route
        
#Define route using 'start' and 'end' as a variables
@app.route('/api/v1.0/<start>/<end>', methods=['GET'], endpoint='start_end')
def start(start,end):
    session = Session(engine)
    # Ensuring that the session is closed after the operation
    try:
        # Querying min, max, and avg temperatures from the start date to the end of the dataset
        results = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
                         filter(measurement.date >= start).\
                         filter(measurement.date<=end).all()

        # Unpacking the result tuple
        min_temp, max_temp, avg_temp = results[0]
        return jsonify({
            "Minimum Temperature": min_temp, 
            "Maximum Temperature": max_temp, 
            "Average Temperature": avg_temp
        })
    finally:
        session.close()


if __name__ == "__main__":
    app.run(debug=True)
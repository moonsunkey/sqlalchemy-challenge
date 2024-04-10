# API Dynamic Route (15 points)
# To receive all points, your Flask application must include
# A start route that:

# Accepts the start date as a parameter from the URL (2 points)

# Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset (4 points)

# A start/end route that: Accepts the start and end dates as parameters from the URL (3 points)

# Returns the min, max, and average temperatures calculated from the given start date to the given end date (6 points)

# Place imports at the top of the file, just after any module comments and docstrings, and before module globals and constants. (2 points)

# Import the dependencies.

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

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

# Session = sessionmaker(bind=engine)
# session = Session()
# print(session.bind)

session = Session(engine)

#Calculate the date one year before the most recent data in the database first

most_recent_date = session.query(func.max(Measurement.date)).scalar()
one_year_before = func.date(most_recent_date, text("'-365 days'"))
session.close()
#################################################
# Flask Setup
#################################################

from flask import Flask

app = Flask(__name__)
#################################################
# Flask Routes
#################################################

# Display the available routes on the landing page 
# A precipitation route that:
# Returns json with the date as the key and the value as the precipitation (3 points)
# Only returns the jsonified precipitation data for the last year in the database (3 points)

# A stations route that:
# Returns jsonified data of all of the stations in the database (3 points)

# A tobs route that:
# Returns jsonified data for the most active station (USC00519281) (3 points)
# Only returns the jsonified data for the last year of data (3 points)



@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    return

@app.route("/jsonified")
def jsonified():
    return jsonify(hello_dict)

if __name__ == "__main__":
    app.run(debug=True)
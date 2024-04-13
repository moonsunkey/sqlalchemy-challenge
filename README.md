# sqlalchemy-challenge
In  this challenge, we are using SQLAlchemy to connect and reflect and query the hawaii.sqlite databse. Link Python to the database by creating a SQLAlchemy session.
Part 1: Analyze and Explore the Climate Data
In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:

Precipitation Analysis
Find the most recent date in the dataset.

Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.


Load the query of "date" and "prcp" values into a Pandas DataFrame. Explicitly set the column names.

Sort the DataFrame values by "date".

Plot the results by using the DataFrame plot method, as the following image shows:

![Precipitation Chart](SurfsUp/precipitation.png)


Use Pandas describe function to print the summary statistics for the precipitation data.

Station Analysis
Design a query to calculate the total number of stations in the dataset.

Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:

List the stations and observation counts in descending order.



Answer the following question: which station id has the greatest number of observations?
Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.

HINT
Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:

Filter by the station that has the greatest number of observations.

Query the previous 12 months of TOBS data for that station.

Plot the results as a histogram with bins=12, as the following image shows:

A screenshot depicts the histogram.



Part 2: Design Your Climate App
Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create 5 routes as follows:


A homepage that lists all the available routes.

/api/v1.0/precipitation

Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

Return the JSON representation of your dictionary.

/api/v1.0/stations

Return a JSON list of stations from the dataset.
/api/v1.0/tobs

Query the dates and temperature observations of the most-active station for the previous year of data.

Return a JSON list of temperature observations for the previous year.

/api/v1.0/<start> and /api/v1.0/<start>/<end>

Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

Hints
Join the station and measurement tables for some of the queries.

Use the Flask jsonify function to convert your API data to a valid JSON response object.


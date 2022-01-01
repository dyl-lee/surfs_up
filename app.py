# 1. import dependencies
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# 2. Set up database
engine = create_engine("sqlite:///hawaii.sqlite") #access and query sqlite db
Base = automap_base() #reflect db into classes
Base.prepare(engine, reflect=True) #reflect tables into SQLalchemy

Measurement = Base.classes.measurement #save references to each table
Station = Base.classes.station

session = Session(engine) #create session link from python to db

# 3. Create an app instance, being sure to pass __name__ (magic variable)
app = Flask(__name__)

# 4. Flask routes. Reminder, print statements are only printed server-side, only return statements appear in the browser
@app.route('/')
def welcome():
    print("Server received request for 'Home' page...")
    return(
        f'Welcome to the Climate Analysis API. <br/>'
        f'Available routes: <br/>'
        f'/api/v1.0/precipitation <br/>'
        f'/api/v1.0/stations <br/>'
        f'/api/v1.0/tobs <br/>'
        f'/api/v1.0/temp/start/end <br/>'
    )

@app.route('/api/v1.0/precipitation')
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation} #create dictionary with date as key and precipitation as value
    return jsonify(precip) #returns dictionary as json

@app.route('/api/v1.0/stations')
def stations():
    results = session.query(Station.station).all() #query to get all stations, comes back as list of tuples
    stations = list(np.ravel(results)) #np.ravel flattens results into one-D array then list() creates a list
    return jsonify(stations=stations) #somehow stations=stations is needed to format list into json

@app.route('/api/v1.0/tobs')
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

@app.route('/api/v1.0/temp/<start>')
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all() # the * next to sel indicates multiple results for query, min, max, avg.
        temps = list(np.ravel(results))
        return jsonify(temps)
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
# ctrl+C terminates the server
if __name__ == "__main__":
    app.run(debug=True)

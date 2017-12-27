# Built In Libraries
import json
import re
import time
# Third Party Libraries
from flask import Flask, make_response, render_template
# Project Functions
from bus_schedule_filter import make_stop_filtered_schedule
from bus_schedule import make_schedule

# Initialization
app = Flask(__name__)
app.debug = True


# View + Path
@app.route('/api')
@app.route('/')
def full_schedule():
    schedule = make_schedule()
    return json.dumps(schedule)


@app.route('/api/<stop_id>')
def bus_stop_schedule(stop_id):

    try:
        stop_id = int(stop_id)
    except ValueError:
        return error_response()

    if stop_id not in range(1, 11):
        return error_response()

    minutes_timestamp = time.gmtime(time.time()).tm_min
    schedule = make_stop_filtered_schedule(minutes_timestamp, stop_id)
    
    response = make_response(json.dumps(schedule))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


def error_response():
    return make_response('404 Not Found - Use Bus Stop ID from 1 to 10', 404)


@app.route('/client')
def pretend_client():
    stop_ids = [1, 2]
    schedule = {}
    
    for stop_id in stop_ids:
        minutes_timestamp = time.gmtime(time.time()).tm_min
        stop_schedule = make_stop_filtered_schedule(minutes_timestamp, stop_id)
        schedule[stop_id] = format_(stop_schedule)

    return render_template('client.html', schedule=schedule)


def format_(routes_schedule):
    formatted = {}
    
    for route, minutes in routes_schedule.items():
        route_match = re.search('\w(\d*)', route)
        route_id = route_match.groups()[0]
        formatted[route_id] = f'{minutes[0]} min, {minutes[1]} min'
    
    return formatted


if __name__ == '__main__':
    app.run()

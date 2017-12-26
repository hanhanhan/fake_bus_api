# Built In Libraries
import json
import time
# Third Party Libraries
from flask import Flask, make_response, render_template
# Project Functions
from bus_schedule_filter import make_stop_filtered_schedule


# Initialization
app = Flask(__name__)
app.debug = True


# View + Path
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
    
    # NOTE: putting in decorator would be nice
    response = make_response(json.dumps(schedule))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


def error_response():
    return make_response('404 Not Found - Use Bus Stop ID from 1 to 10', 404)


@app.route('/client')
def pretend_client():
    placeholder = '5'
    bus_stops = [1, 2]
    return render_template('client.html', **{
        'bus_stops': bus_stops,
        'r1_times': f'{placeholder} min, {placeholder} min',
        'r2_times': f'{placeholder} min, {placeholder} min',
        'r3_times': f'{placeholder} min, {placeholder} min',
        })


if __name__ == '__main__':
    app.run()

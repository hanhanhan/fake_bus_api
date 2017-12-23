# Built In Libraries
import json
import time
# Third Party Libraries
from flask import Flask, make_response
# Project Functions
from helper_functions import make_stop_filtered_schedule


# Initialization
app = Flask(__name__)

# View + Path
@app.route('/<stop_id>')
def bus_stop_schedule(stop_id):

    try:
        stop_id = int(stop_id)
    except ValueError:
        return error_response()

    if stop_id not in range(1, 11):
        return error_response()

    minutes_timestamp = time.gmtime(time.time()).tm_min
    schedule = make_stop_filtered_schedule(minutes_timestamp, stop_id)
    return json.dumps(schedule)


def error_response():
    return make_response('404 Not Found - Use Bus Stop ID from 1 to 10', 404)



if __name__ == '__main__':
    app.run()

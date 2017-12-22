# Built In Libraries
import json
import time
# Third Party Libraries
from flask import Flask
from flask_socketio import SocketIO
# Project Functions
from bus_schedule_builder import make_schedule
from helper_functions import make_stop_filtered_schedule


# Initialization
app = Flask(__name__)
socketio = SocketIO(app)

# Route
@app.route('/<stop_id>')
def hello(stop_id):
    try:
        stop_id = int(stop_id)
    except ValueError:
             return '404 Not Found - Use Bus Stop ID from 1 to 10'

    if stop_id not in range(1, 11):
        return '404 Not Found - Use Bus Stop ID from 1 to 10'

    minutes_timestamp = time.gmtime(time.time()).tm_min
    schedule = make_stop_filtered_schedule(minutes_timestamp, stop_id)
    return json.dumps(schedule)

if __name__ == '__main__':
    socketio.run(app)

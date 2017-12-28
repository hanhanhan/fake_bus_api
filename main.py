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
    timestamp = time.gmtime(time.time()).tm_min
    api_data = {'schedule': schedule, 'timestamp': timestamp}

    response = make_response(json.dumps(api_data))
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response


if __name__ == '__main__':
    app.run()

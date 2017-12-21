from quart import Quart, g
import json
import time
from bus_schedule_builder import make_schedule


app = Quart(__name__)


def get_nearest_bus_index(timestamp, stop_times):
    index = 0
    while stop_times[index] <= timestamp:
        index += 1
    
    # if index = 0:

    return index

def make_bus_stop_schedule(timestamp, stop_id):
    for route, stops in g.schedule.items():
        schedule[route] = stops[stop_id]

    return schedule


@app.before_request
def before_request():
    g.schedule = make_schedule()


@app.route('/<stop_id>')
async def hello(stop_id):
    try:
        stop_id = int(stop_id)
    except ValueError:
             return '404 Not Found - Use Bus Stop ID from 1 to 10'

    if stop_id not in range(1, 11):
        return '404 Not Found - Use Bus Stop ID from 1 to 10'
    
    minutes_timestamp = time.gmtime(time.time()).tm_min
    schedule = make_bus_stop_schedule(minutes_timestamp, stop_id)

    return json.dumps(schedule)


# @app.websocket('ws')
# async def ws():
#     while True:
#         await websocket.send('hello')

app.run(port=8000)

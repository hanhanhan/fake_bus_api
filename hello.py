from quart import Quart, g
import json
import time
from bus_schedule_builder import make_schedule
from helpers import make_bus_stop_schedule

app = Quart(__name__)


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

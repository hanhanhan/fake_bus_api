# Built In Libraries
import json
# Third Party Libraries
from flask import Flask
from flask_socketio import SocketIO, emit
# Project Functions
from bus_schedule import make_schedule


# Initialization
app = Flask(__name__)
app.debug = True
socketio = SocketIO(app)


@socketio.on('connect')
def handle_message():
    schedule = make_schedule()
    print('sending schedule')
    emit('schedule', schedule)


@app.route('/delay')
def delay():
    schedule = make_schedule()
    for bus_stop, routes in schedule.items():
        for route, times in routes.items():
            for i, time in enumerate(times):
                schedule[bus_stop][route][i] += 5.5
    socketio.emit('schedule', schedule, broadcast=True)
    return 'A 5.5 minute delay was triggered on all routes.'


if __name__ == '__main__':
    socketio.run(app)

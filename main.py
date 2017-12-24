
from flask import Flask, make_response
from flask_socketio import SocketIO, emit, send


# Initialization
app = Flask(__name__)
socketio = SocketIO(app)


@socketio.on('connect')
def test_connect():
    print('connection made')
    emit('my response', {'data': 'Connected'})


@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)


@app.route('/')
def index():
    return 'hi i\'m the index'


@socketio.on('json', namespace='/living_room')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)


if __name__ == '__main__':
    socketio.run(app)

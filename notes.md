websockets

All client connections go to same URL?
information is sent (vanilla websockets)/emitted (named function)

send from server at interval -- yield, while loop?

send to server from client -- second ws route?

client:
where in the document should I initialize the connection?
does using broadcast lessen connections?

testing recommendations


---------------

export FLASK_DEBUG=1 (or not!), secret key
export FLASK_APP=main.py
flask run

websocket command line client
$ wscat -c ws://echo.websocket.org -p 13
----------------

Try flask-socketio
env is fake_bus

without geventlet:
>python hello.py
WebSocket transport not available. Install eventlet or gevent and gevent-websocket for improved performance.

>pip install eventlet
>python hello.py 
program hangs

>FLASK_APP=hello.py flask run
ImportError: No module named 'flask_socketio'

> pip freeze
certifi==2016.2.28
click==6.7
enum-compat==0.0.2
eventlet==0.21.0
Flask==0.12.2
Flask-SocketIO==2.9.3
greenlet==0.4.12
itsdangerous==0.24
Jinja2==2.10
MarkupSafe==1.0
python-engineio==2.0.1
python-socketio==1.8.4
six==1.11.0
Werkzeug==0.13

python=3.6

>pip uninstall eventlet

https://github.com/miguelgrinberg/Flask-SocketIO/issues/164

---------------

<!-- https://stackoverflow.com/questions/10175812/how-to-create-a-self-signed-certificate-with-openssl -->

<!-- https://stackoverflow.com/questions/21297139/how-do-you-sign-certificate-signing-request-with-your-certification-authority/21340898#21340898 -->

openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365


Create your own authority (i.e, become a CA)
Create a certificate signing request (CSR) for the server
Sign the server's CSR with your CA key
Install the server certificate on the server
Install the CA certificate on the client


----
ssh -i  /Users/hannah/.ssh/throwaway root@107.170.208.230
ssh -i /Users/hannah/.ssh/throwaway hannah@107.170.208.230 

ssh -i /path_to/daniels_throwaway_key daniel@107.170.208.230

----
python3.6 alias

------
make a dictionary
bus stops, list of buses
at each 15 minute interval, push a bus onto the route 1 
two minutes after, push bus onto route 2,
two minutes after, push bus onto route 3

every two minutes, move bus to next stop

bus gets to stop 10 then remove it

15 30 45






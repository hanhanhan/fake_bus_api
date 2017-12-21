import ssl
from quart import Quart


app = Quart(__name__)


@app.route('/')
async def hello():
    return 'hello'


# @app.websocket('ws')
# async def ws():
#     while True:
#         await websocket.send('hello')

ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_COMPRESSION
ssl_context.set_ciphers('ECDHE+AESGCM')
# name is from Privacy Enhanced Mail (PEM), a failed method for secure email but the container format it used lives on, and is a base64 translation of the x509 ASN.1 keys
# key This is a PEM formatted file containing just the private-key of a specific certificate and is merely a conventional name 
ssl_context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
ssl_context.set_alpn_protocols(['h2', 'http/1.1'])
app.run(port=5000, ssl=ssl_context)

# app.run(port=5000)
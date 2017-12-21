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






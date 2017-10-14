#Creating a web server using python

#we need to first import the socket library
import socket

#next we need to create a socket object
s = socket.socket()
#we get the local machine name
#host = socket.gethostname()
print("Socket successfully created")

#Next reserve a port for the socket connection to use:
port = 23456

#Next bind the socket to this port
#empty string allows server listen to requests from other computers on the network.
s.bind(('', port))
print("Socket bound to %s" %(port))

#After binding we need to put our socket into listening mode
s.listen(5)
print("Socket is now in listening mode")

#create a while loop that runs indefinitely to establish connection with a client
while True:
    c, addr = s.accept()
    print("Connection received from", addr)
    c.close()

#We create a socket script that we can use to connect to any website

#We need to import the socket and sys modules
import socket
import sys

#SOCK_STREAM used for connection oriented protocols
#AF_INET protocol specifies address group (IPv4)
#SOCK_STREAM establishes connection between our host and the website
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
#account for any connection errors
except socket.error as err:
    print("Socket creation unsuccessful due to an error %s" %(err))

#specify and bind socket to a default port.
#we use the default http port 80 since we are trying to establish http connection
port = 80

#now we try to connect to the website
#we use gethostbyname since we are using the unresolved website name
try:
    host = socket.gethostbyname('www.facebook.com')
#Account for domain name resolution error for the host
except socket.gaierror:
    print("There was an error resolving the host")
    sys.exit()

#establishing connection with the web server
s.connect((host, port))
print("We have successfully connected to facebook on: %s" %(host))

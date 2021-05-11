#!/usr/bin/python
import socket

#socket object
#sock initialized as a socket composed of IPv4 address and TCP packets

#initialize host and port
host = raw_input("Enter the Host to Scan: ")
#port = int(raw_input("Enter the Port to Scan: "))

#create function to scan port
for port in range(1,1000):
	#check to see if connection was established
	#if you get an error the port is closed else port is open
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(.5)
	if soc.connect_ex((host,port)):
		print "port %d is closed" % (port)
	else:
		print "port %d is open" % (port)
	soc.close()


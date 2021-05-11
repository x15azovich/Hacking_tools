#!/usr/bin/python

import socket


def returnBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		#connect to the ip and port with a socket
		s.connect((ip,port))
		#recieve bytes from target and store in banner variable
		banner = s.recv(1024)
		return banner
	except:
		return


def main():

	ip = raw_input("Enter Target IP address: ")
	for x in range(0,100):
		banner = returnBanner(ip, x)
		if banner:
			print "Successfully returned Value: " + banner + "For port " + str(x)


main()	

#!/usr/bin/python
from socket import *
import optparse
from threading import *

def portScan(targetHost, targetPort):
	#resolve domain name
	try:
		#get the target IP with domain/target name
		targetIP=gethostbyname(targetHost)
	except:
		print "Unkown host %s " %targetHost
	try:
		#get the hostname from the address
		targetName=gethostbyaddr(targetIP)
		print 'Scan Results For: ' + targetName[0]
	except:	
		print 'scan Results for: ' + targetIP
	setdefaulttimeout(1)
	for port in targetPort:
		#create a new thread to scan the ports
		t = Thread(target=connScan, args=(targetHost, int(port)))
		t.start()



def connScan(targetHost, targetPort):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((targetHost, targetPort))
		print '%d/tcp Open' %targetPort
		print 'banner is : ' + sock.recv(1024)
		sock.close()
	except:
		print '%d/tcp Closed' %targetPort
	finally:
		sock.close()


def main():
	#create the parser object
	parser = optparse.OptionParser('Uage of program: ' + '-H <target host> -p <target port>')
	#create option to append to the parser
	parser.add_option('-H', dest='targetHost', type = 'string', help='specify target host name')
	parser.add_option('-p', dest='targetPort', type = 'string', help='specify target port numbers seperated by a comma')
	#parse the arguements
	(options, args) = parser.parse_args()
	#initialize the variabels in the options
	targetHost=options.targetHost
	targetPorts=str(options.targetPort).split(',')
	if (targetHost == None) | (targetPorts[0] == None):
		print parser.usage
		exit(0)
	portScan(targetHost,targetPorts)

if __name__== '__main__':
	main()



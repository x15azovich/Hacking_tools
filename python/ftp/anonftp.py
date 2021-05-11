#!/usr/bin/python
import ftplib


def anonLogin(hostname):
	try:
		ftp=ftplib.FTP(hostname)
		ftp.login('anonymus', 'anonymus')
		print("[*] " + hostname +" Ftp Anonymus Login Successful ")
		ftp.quit()
		return True
	except Exception, e:
		print ("[-] " + hostname +" FTP Anonymus Login Failed ")

host = raw_input("Enter the IP Address: ")
anonLogin(host)


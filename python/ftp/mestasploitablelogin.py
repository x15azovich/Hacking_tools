#!/usr/bin/python
import ftplib


def anonLogin(hostname):
	try:
		ftp=ftplib.FTP(hostname)
		ftp.login('msfadmin', 'msfadmin')
		print("[*] " + hostname +" Ftp Anonymus Login Successful ")
		ftp.quit()
		return True
	except:
		print ("[-] " + hostname +" FTP Anonymus Login Failed ")

host = input("Enter the IP Address: ")
anonLogin(host)


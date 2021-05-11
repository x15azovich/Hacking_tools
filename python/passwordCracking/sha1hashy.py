#!/usr/bin/python
#read from internet
from urllib.request import urlopen
import hashlib
#from termcolor import colored

sha1hash = input("[*] Enter the Sha1Hash Value: ")
passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')
for line in passlist.split('\n'):
	hashguess = hashlib.sha1(bytes(line, 'utf-8')).hexdigest()
	if hashguess==sha1hash:
		print("[+] Password is: " + str(line))
		quit()
	else:
		print("[-] Password guess " + str(line) + " Does not match")
print("Password not in the password list")


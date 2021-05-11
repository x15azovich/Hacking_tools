#!/usr/bin/python
import requests

def request(url):
	try:
		return requests.get("http://" +url)
	except requests.exceptions.ConnectionError:
		pass


file_name = raw_input("Enter the file to use : ")
target_url = raw_input("Enter the target URL: ")
file = open(file_name,"r")
for word in file:
	word=word.strip()
	full_url = word + "." + target_url
	response = request(full_url)
	if response:
		print("[+] Discovered subdomain at this link: " + full_url)


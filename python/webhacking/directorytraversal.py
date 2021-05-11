#!/usr/bin/python
import requests

def request(url):
	try:
		return requests.get("http://" +url)
	except requests.exceptions.ConnectionError:
		pass



target_url = raw_input("Enter the target URL: ")
file = open("common.txt","r")
for word in file:
	word=word.strip()
	full_url = target_url + "/" + word
	response = request(full_url)
	if response:
		print("[+] Discovered directory at this link: " + full_url)


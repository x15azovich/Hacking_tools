#!/user/bin/python

import hashlib

def tryOpen(pass_list):
	global pass_file
	try:
		pass_file = open(pass_list, "r")
	except:
		print("[!] No such file path exists ")

pass_hash= input("Enter MD5 Hash Value : ")
pass_list= input("Enter the password list: ")
tryOpen(pass_list)

for word in pass_file:
	print("Trying: " + word.strip('\n'))
	enc_word = word.encode('utf-8')
	md5hash = hashlib.md5(enc_word.strip()).hexdigest()
	if md5hash == pass_hash:
		print("Password has been found: " + word)
		exit(0)
print("Password is not in the list")


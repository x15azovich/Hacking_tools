#!/usr/bin/python

import crypt


def crackPass(cryptWord):
	#find salt
	salt = cryptWord[0:2]
	dictionary = open("dictionary.txt", 'r')
	for word in dictionary.readlines():
		word = word.strip('\n')
		cryptPass = crypt.crypt(word, salt)
		if(cryptWord == cryptPass):
			print("[+] Password has been found: " + word)
			return


def main():
	password_file = open('passwords.txt', 'r')
	for line in password_file.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptWord = line.split(':')[1].strip('\n')
			print("[*] Cracking Password for : " + user +" With password " + cryptWord)
			crackPass(cryptWord)
main()

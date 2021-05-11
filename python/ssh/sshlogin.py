#!/usr/bin/python

import pexpect

PROMPT=['# ', '>>> ', '> ', '\$ ']


def send_command(child,command):
	child.sendline(command)
	child.expect(PROMPT)
	print child.before

def connect(user, host, password):
	ssh_newkey = 'Are you sure you want to continue connecting'
	connStr = 'ssh ' + user  + '@' + host
	child = pexpect.spawn(connStr)
	ret = child.expect([pexpect.TIMEOUT , ssh_newkey, '[P|p]assword: '])
	if ret==0:
		print '[-] Error Connection'
	if ret==1:
		child.sendline('yes')
		ret = child.expect([pexpect.TIMEOUT,'[P|password: '])
		if ret==0:
			print '[-] Error Connection'
			return
	child.sendline(password)
	child.expect(PROMPT)
	return child

def main():
	host = raw_input("Enter the Hostname: ")
	user = raw_input("Enter the SSH username: ")
	password = raw_input("Enter the password: ")
	command = raw_input("Enter the command you wish to run: ")
	child = connect(user,host,password)
	send_command(child, command)

main()


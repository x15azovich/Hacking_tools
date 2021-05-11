#!/usr/bin/python
import subprocess

def change_mac_address(interface,mac):
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",mac])
	subprocess.call(["ifconfig",interface,"up"])

def main():
	interface = input("Please enter the interface: ")
	new_mac_address = input("Enter the mac address you want: ")
	currentAddress= subprocess.check_output(["ifconfig",interface])
	change_mac_address(interface,new_mac_address)
	after_change = subprocess.check_output(["ifconfig",interface])
	if currentAddress == after_change:
		print("Failed to change the mac address to  " + new_mac_address )
	else:
		print("Mac address successfully changed top " + new_mac_address+ " On Interface " + interface)

main()

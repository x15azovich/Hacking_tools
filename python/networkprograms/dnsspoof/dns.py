#!/usr/bin/python
from scapy.all import *


def findDNS(packet):
	if packet.haslayer(DNS):
		print(packet[IP].src, packet[DNS].summary())

sniff(prn=findDNS)

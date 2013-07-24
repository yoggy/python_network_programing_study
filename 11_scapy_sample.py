#!/usr/bin/python
#
# 11_scapy_sample.py - sample program using scapy
#
# scapy
#     http://www.secdev.org/projects/scapy/portability.html
#
# install (debian, ubuntu)
#     $ sudo apt-get install python-scapy
#
# usage
#     $ ./11_scapy_sample.py
#     usage : ./11_scapy_sample.py pcap_file port check_string
#
#     $ ./11_scapy_sample.py defcon_20-ctf-0566.pcap 24359 rflr
#     (cherry)

import sys
import time
from string import printable
from pprint import pprint
from scapy.all import *

if len(sys.argv) < 4:
	print "usage : ./11_scapy_sample.py pcap_file port check_string"
	print ""
	exit(1)

pr = PcapReader(sys.argv[1])
port = int(sys.argv[2])
check_string = sys.argv[3]

while True:
	p = pr.read_packet()
	if p is None: break;

	if TCP in p and (p[TCP].sport == port or p[TCP].dport == port):
		# check payload
		if hasattr(p[TCP], "load"):
			payload = p[TCP].load

			# check
			if check_string in payload:
				# print packet
				print "======== %s ========" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(p.time))
				p.show()
				#hexdump(p)
			
			# check printable
			if all(c in printable for c in payload) == False:

				# print packet
				print "======== %s ========" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(p.time))
				p.show()
				#hexdump(p)
	


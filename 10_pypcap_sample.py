#!/usr/bin/python
#
# 10_pypcap_sample.py - sample program for pcap file handling
#
# pypcap
#     http://code.google.com/p/pypcap/
#
# install (debian or ubuntu)
#     $ sudo apt-get install python-pypcap python-dpkt
#
# usage
#     $ ./10_pypcap_sample.py
#     usage : ./10_pypcap_sample.py pcap_file port check_string
#
#     $ ./10_scapy_sample.py defcon_20-ctf-0566.pcap 24359 rflr
#     (cherry)
#
import sys
import time
from string import printable
from pprint import pprint
import dpkt, pcap

if len(sys.argv) < 4:
	print "usage : ./10_pypcap_sample.py pcap_file port check_string"
	print ""
	exit(1)

pc = pcap.pcap(sys.argv[1])
port = int(sys.argv[2])
check_string = sys.argv[3]

for t, p in pc:
	ether = dpkt.ethernet.Ethernet(p)

	if isinstance(ether.data, dpkt.ip6.IP6):
		ipv6 = ether.data
		
		if isinstance(ipv6.data, dpkt.tcp.TCP):
			tcp = ipv6.data

			if tcp.sport == port or tcp.dport == port:
				# check string
				if check_string in tcp.data:
					print "======== %s ========" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))
					pprint(tcp.data)
	
				# check printable
				if all(c in printable for c in tcp.data) == False:
					print "======== %s ========" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))
					pprint(tcp.data)



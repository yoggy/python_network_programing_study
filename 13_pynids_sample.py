#!/usr/bin/python
#
# 13_pynids_sample.py - pynids sample program
#
# pynids
#   http://jon.oberheide.org/pynids/
#
# install (debian or ubuntu)
#   $ sudo apt-get install python-nids
#
# notes
#   libnids does not support IPv6...
#

import sys
import nids
from pprint import pprint

def TcpHandler(tcp):
	if tcp.nids_state == nids.NIDS_JUST_EST:
		tcp.server.collect = 1
		tcp.client.collect = 1
	elif tcp.nids_state == nids.NIDS_DATA:
		tcp.discard(0)  # keep data
	elif tcp.nids_state in [nids.NIDS_CLOSE, nids.NIDS_TIMEOUT, nids.NIDS_RESET]:
		((src, sport), (dst, dport)) = tcp.addr
		print "==========================(%s:%d <--> %s:%d)==========================" % (src, sport, dst, dport)
		print tcp.server.data[:tcp.server.count]
		print tcp.client.data[:tcp.client.count]

if len(sys.argv) < 2:
	print("usage : ./13_pynids_sample.py pcap_file")
	print("")
	exit(1)

# set libnids parameters
#nids.param("pcap_filter", "tcp")
nids.param("scan_num_hosts", 0)
nids.chksum_ctl([('0.0.0.0/0', False), ('::', False)])
nids.param("filename", sys.argv[1])
print "pcap_file=%s" % sys.argv[1]

nids.init()

nids.register_tcp(TcpHandler)

nids.run()


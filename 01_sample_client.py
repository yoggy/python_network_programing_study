#!/usr/bin/python

import sys
import socket
from time import sleep

if len(sys.argv) < 3:
	print "usage : ./01_sample_client.py host port"
	print
	exit(1)

host = sys.argv[1]
port = int(sys.argv[2])

# create socket
sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)    # for IPv6
#sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)   # for IPv4

sock.connect((host, port))

while True:
	recv_data = ""

	# read message from server
	sleep(0.2)
	while True:
		d = sock.recv(1024)
		print d
		recv_data += d
		if "> "  in recv_data: break
		if "key" in recv_data: break
	
	# create answer string
	for l in recv_data.splitlines():
		# find "numbers : 1 2 3" line
		if "numbers :" in l:
	
			# split numbers
			numstr = l.split(":")[1].strip().split(" ")
			num = [int(s) for s in numstr]
	
			# sort numbers & create answer string
			ans = sorted(num)
			ansstr = " ".join([str(n) for n in ans])
			break

		# print key if you got key string
		if "congraturation" in l:
			key = l.split("=")[1].strip()
			print "!!!!!!!! key is %s !!!!!!!!" % key
			exit(0)
	
	# send anser
	print "send : %s" % ansstr
	sock.sendall(ansstr + "\r\n")


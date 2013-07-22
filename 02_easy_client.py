#!/usr/bin/python
import sys
import easy_tcp

if len(sys.argv) < 3:
	print "usage : ./02_easy_client.py host port"
	exit(1)

host = sys.argv[1]
port = int(sys.argv[2])

# connect to server
sock = easy_tcp.connect(host, port)

while True:
	# read message from server
	recv_data = sock.recv()
	
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
	sock.sendln(ansstr)
	

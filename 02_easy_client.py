#!/usr/bin/python

import easy_tcp

# connect to server
socket = easy_tcp.connect("::1", 12345)

while True:
	# read message from server
	msg = socket.recv()
	
	# create answer string
	for l in msg.splitlines():
		# find "numbers : 1 2 3" line
		if "numbers :" in l:
	
			# split numbers
			numstr = l.split(":")[1].strip().split(" ")
			num = [int(s) for s in numstr]
	
			# sort numbers & create answer string
			ans = sorted(num)
			ansstr = " ".join([str(n) for n in ans])
			break

		# if you got key string
		if "congraturation" in l:
			key = l.split("=")[1].strip()
			print "!!!!!!!! key is %s !!!!!!!!" % key
			exit(0)
	
	# send anser
	socket.sendln(ansstr)
	

#!/usr/bin/python

import easy_tcp

# connect to server
s = easy_tcp.connect("::1", 12345)

# read message from server (1.0 is read_timeout)
msg = s.recv(1.0) 
s.send("123")

s.close()

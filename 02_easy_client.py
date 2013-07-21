#!/usr/bin/python

# for easy_tcp
from easy_tcp import connect
from easy_tcp import send
from easy_tcp import recv
from easy_tcp import close

# connect to server
connect("::1", 12345)

# read message from server (1.0 is read_timeout)
msg = recv(1.0) 

send("123")

close()

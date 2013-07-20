#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.connect(("::1", 12345))

print s.recv(1024)
s.close()


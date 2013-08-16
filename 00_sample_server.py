#!/usr/bin/python
import socket
import signal
from random import randint
from timeout import timeout
from timeout import TimeoutError
from SocketServer import BaseRequestHandler
from SocketServer import TCPServer

class NotImplementedError(Exception):
	pass

class Session:
	def __init__(self, client_address, request):
		self.client_address = client_address
		self.request = request

	def send(self, data):
		return self.request.send(data)

	def sendln(self, data):
		return self.request.send(data+"\r\n")

	def recv(self):
		self.send("> ")
		return self.request.recv(2048)

	def on_connect(self):
		raise NotImplementedError()

class SampleSession(Session):
	def __init__(self, client_address, request):
		Session.__init__(self, client_address, request)

	def send_banner(self):
		self.sendln("+---------------------------------------+")
		self.sendln("|                                       |")
		self.sendln("|   welcome to sorting problem server   |")
		self.sendln("|                                       |")
		self.sendln("+---------------------------------------+")

	def generate_numbers(self, count):
		self.numbers = []
		for i in range(count + 3):
			self.numbers.append(randint(1, 200))
		
		self.answer = sorted(self.numbers)
		self.answer_str = " ".join([str(v) for v in self.answer])

	def send_problem(self, count):
		self.sendln("\r\nplease sort numbers in ascending order.")

		self.generate_numbers(count)
		self.send("numbers : ")
		for n in self.numbers:
			self.send(str(n))
			self.send(" ")
		self.send("\r\n")

	def check_answer(self, str):
		str = str.strip()
		if self.answer_str == str:
			return True
		return False

	def on_connect(self):
		self.send_banner()

		for i in range(30):
			self.send_problem(i)
			res = self.recv()
			if self.check_answer(res) == False:
				self.sendln("wrong answer...")
				return
			else:
				self.sendln("correct answer!!")
		self.sendln("\r\ncongraturation!!! key=85fafe70367a388d5df98c4dfa11eac7")

class SampleHandler(BaseRequestHandler):
	@timeout(60)
	def loop(self, session):
		session.on_connect()
		session.sendln("bye bye")

	def handle(self):
		print "connect : %s" % self.client_address[0]
		session = SampleSession(self.client_address, self.request)
		self.loop(session)
		print "disconnect : %s" % self.client_address[0]

class TCPServer(TCPServer):
	allow_reuse_address = True

class TCPServer6(TCPServer):
	address_family = socket.AF_INET6

if __name__ == "__main__":
	#server = TCPServer(("127.0.0.1", 12345), SampleHandler)
	server = TCPServer6(("::1", 12345), SampleHandler)
	server.serve_forever()



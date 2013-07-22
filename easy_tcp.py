import sys
import socket
import select

# log setting
easy_tcp_output_log_level = 0

def is_disable_output(my_level):
	global easy_tcp_output_log_level
	if my_level < easy_tcp_output_log_level:
		return True
	return False

def log_e(name, msg): 
	if is_disable_output(2): return
	print "easy_tcp[E] %s() : %s" % (name, msg)

def log_i(name, msg): 
	if is_disable_output(1): return
	print "easy_tcp[I] %s() : %s" % (name, msg)

def log_d(name, msg): 
	if is_disable_output(0): return
	print "easy_tcp[D] %s() : %s" % (name, msg)

def connect(host, port):
	log_d("connect", "host=%s, port=%d" % (host, port))

	res = socket.getaddrinfo(host, str(port))

	s = None
	err = ""
	for (ai_family, ai_socket_type, ai_protocol, ai_canonname, ai_addr) in res:
		try:
			# check addrinfo
			if ai_family != socket.AF_INET6 and ai_family != socket.AI_INET:
				continue
			if ai_socket_type != socket.SOCK_STREAM:
				continue

			s = socket.socket(ai_family, ai_socket_type)
			if s < 0:
				s = None
				continue

			s.connect((ai_addr[0], ai_addr[1]))
			break
		except Exception as e:
			err = e
			s = None

	if s is None:
		log_e("connect", "connect() failed...err=%s" % err)
		sys.exit(1)

	s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

	tcp = EasyTCP(s, host, port)
	log_i("connect", "connect() success...host=%s, port=%d" % (host, port))
	return tcp
	
class EasyTCP:
	def __init__(self, socket, host, port):
		self.socket = socket
		self.host   = host
		self.port   = port

	def __del__(self):
		self.close()

	def send(self, data):
		log_d("send", "data=%s" % data)
		try:
			self.socket.sendall(data)
		except Exception as e:
			log_e("send", "send() failed...err=%s" % e)
			sys.exit(1)

	def sendln(self, data):
		data = data + "\r\n"
		self.send(data)
	
	def recv(self, read_timeout=0.5):
		self.socket.setblocking(0)
		
		data = ""

		is_first = True;
	
		try:
			while True:
				t = read_timeout
				if is_first: t = t * 10.0

				r = select.select([self.socket], [], [], t)

				is_first = False

				if r[0]:
					d = self.socket.recv(1024)
					if len(d) > 0:
						data += d
					else:
						break
				else:
					break
		except Exception as e:
			log_e("recv", "recv() failed...err=%s" % e)
			sys.exit(1)
			
		log_d("recv", "size=%d, data=%s" % (len(data), data))
		return data

	def close(self):
		try:
			if self.socket is not None:
				self.socket.close()
				self.socket = None
				log_i("close", "close socket...host=%s, port=%d" % (self.host, self.port))
				self.host = ""
				self.port = -1
		finally:
			pass


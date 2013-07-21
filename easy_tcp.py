import sys
import socket
import select

# log setting
easy_tcp_output_log_level = 0

# global object...
easy_tcp_host_   = ""
easy_tcp_port_   = -1
easy_tcp_socket_ = None

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

def socket_check():
	global easy_tcp_socket_
	if easy_tcp_socket_ is None:
		log_e("recv", "please connect() first!. socket is None...")
		sys.exit(1)

def connect(host, port):
	global easy_tcp_host_, easy_tcp_port_, easy_tcp_socket_

	log_d("connect", "host=%s, port=%d" % (host, port))

	res = socket.getaddrinfo(host, str(port))

	s = None
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
			print e
			s = None

	if s is None:
		log_e("connect", "connect() failed...host=%s, port=%d" % (host, port))
		sys.exit(1)

	s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

	easy_tcp_host_ = host
	easy_tcp_port_ = port
	easy_tcp_socket_ = s

	log_i("connect", "connect() success...host=%s, port=%d" % (host, port))
	
def close():
	global easy_tcp_host_, easy_tcp_port_, easy_tcp_socket_

	if easy_tcp_socket_ is not None:
		easy_tcp_socket_.close()
		easy_tcp_socket_ = None
		log_i("close", "close socket...host=%s, port=%d" % (easy_tcp_host_, easy_tcp_port_))
		easy_tcp_host_ = ""
		easy_tcp_port_ = -1

def send(data):
	global easy_tcp_socket_
	socket_check()

	log_d("send", "data=%s" % data)
	easy_tcp_socket_.sendall(data)

def recv(read_timeout=0.5):
	global easy_tcp_socket_
	socket_check()

	easy_tcp_socket_.setblocking(0)
	
	data = ""

	while True:
		r = select.select([easy_tcp_socket_], [], [], read_timeout)
		if r[0]:
			d = easy_tcp_socket_.recv(1024)
			if len(d) > 0:
				data += d
			else:
				break
		else:
			break
	log_d("recv", "data=%s" % data)
	return data
	

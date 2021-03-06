#!/usr/bin/env python

#Socket Server Multithreading

#First we will create a Server script so that the client can communicate with it. We will need to import the socket library to establish a connection and the thread
#library for multithreading


import socket
from threading import Thread
from SocketServer import ThreadingMixIn

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):
	def __init__(self,ip,port):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		print "[+] New server socket thread started for " + ip + ":" + str(port)

	def run(self):
		while True:
			data = conn.recv(2048)
			print "Server received data:", data
			MESSAGE = raw_input("Multithreaded Python server: Enter Response from Server/Enter exit:")
			if MESSAGE == 'exit':
				break
			conn.send(MESSAGE) 	#	echo


# Multhithreaded Python server: TCP Server Socket Program Stub
TCP_IP = '127.0.0.1'
TCP_PORT = 2004
BUFFER_SIZE = 20 	# Usually 1024, but we need quick response

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

while True:
	tcpServer.listen(4)
	print "Multithreaded Python server : Waiting for connections from TCP clients..."
	(conn, (ip, port)) = tcpServer.accept()
	newthread = ClientThread(ip, port)
	newthread.start()
	thread.append(newthread)

for t in threads:
	t.join()


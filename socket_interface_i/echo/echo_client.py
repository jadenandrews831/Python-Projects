#!/usr/bin/env python3

#In comparison to the server, the client is pretty simple. It creates a socket
#object, connects to the server and calls s.sendall() to send its message.

import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall(b'Hello, world')
	data = s.recv(1024)

print('Received', repr(data))

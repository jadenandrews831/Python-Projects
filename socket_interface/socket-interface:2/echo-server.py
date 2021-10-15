#!/usr/bin/python3

import socket

#The 'HOST' and 'PORT' make up the host IP Address and port number to access the process. 
#This information is used with the socket.bind() method. Because the Address Family is for
#IPv4, the s.bind() method expects a tuple containing the IPv4 address and port number
#If the Address family were different, the s.bind() method would expect different parameters.

HOST = '127.0.0.1' # Standard loopback interface address (localhost)
PORT = 65432

#socket.socket() creates a socket object of type context manager (it's a python thing...). 
#This allows for the allocation and distribution of resources precisely when you want to.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen() # enables a server to use the accept() method. The socket is now "listening"
	conn, addr = s.accept() #
	with conn:
		print('Connected by', addr)
		while True:
			data = conn.recv(1024)
			if not data:
				break
			conn.sendall(data)

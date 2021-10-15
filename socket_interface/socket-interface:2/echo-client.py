#!/usr/bin/python3

#The echo client has the limitation of receiving one response from a server, then exiting

#Applications are responsible for checking that all data has been sent; if only some of the data
#was transmitted, the application needs to attempt delivery of the remaining data.≈

import socket

HOST='127.0.0.1'
PORT=65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST,PORT))

	#If we had used the .send() method instead, .send() would be limited similarly to the s.recv() statement below
	#.send() returns the number of bytes sent, which may be less than the size of the data passed in.
	#.sendall() Unlike .send() continues to send data from bytes until either all data has been sent or an error occurs. 
	s.sendall(b'Hello, world')

	#When the client makes the following call, it is possible that 's.recv()' will return only one byte, b'H' from b'Hello, world!'
	#The bufsize argument of 1024 used is the maximum amount of data to be received at once. (I think this is the MSS)
	data = s.recv(1024)

print('Received', repr(data))

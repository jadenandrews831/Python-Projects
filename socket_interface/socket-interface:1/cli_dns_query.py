#!/usr/bin/python

import socket
socket.getaddrinfo('www.google.com',80,socket.AF_UNSPEC,socket.SOCK_STREAM)

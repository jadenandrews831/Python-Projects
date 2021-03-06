#!/urs/bin/python3

import selectors
sel = selectors.DefaultSelector()

#*********SETTING UP THE LISTENING SOCKET***************

lsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print('listening on', (host, port))
lsock.setblocking(False)						#to configure the socket in non-blocking mode: a socket is in blocking mode when an I/O call waits for an event to complete. If the blocking mode is set for a socket, the calling program is suspended until the expected event completes.
sel.register(lsock, selectors.EVENT_READ, data=NONE)			#registers the socket to be monitored with sel.select() for the awaited events. selectors.EVENT_READ tells the 'sel' object that it should be looking for read events. Data is used to store whatever arbitrary data you'd like along with the socket. It is returned when select() returns. data is used to keep track of what has been sent and received on the socket.

#*********************EVENT LOOP************************

while True:
	events = sel.select(timeout=None)				#blocks until there are sockets ready for I/O. Returns a list of (key, events) tuples, one for each socket.
	for key, mask in events:					#key is  a SelectorKey namedtuple that contains a fileobj attribute. key.fileobj is the socket object. mask is an event mask of the operations that are ready.
		if key.data is None:					#if key.data is None, then we can identify that it is from the listening socket, and we need to accept() the connection. accept_wrapper() is a made function that will get a new socket object and register it with the selector.
			accept_wrapper(key.fileobj)
		else:							#if key.data is not None, then we know that it is a client socket that has already been accepted, so it must be serviced. service_connection() [provides an unknown service]
			service_connection(key, mask)


def accept_wrapper(sock):
	conn, addr = sock.accept() 					# Should be ready to read since the listening scoket was registered to the selector for the event selectors.EVENT_READ.
	print('accepted connection from ', addr)
	conn.setblocking(false)
	data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
	events = selectors.EVENT_READ | selectors.EVENT_WRITE
	sel.register(conn, events, data=data)


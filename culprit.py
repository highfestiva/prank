#!/usr/bin/env python


import socket
import sys
from threading import Thread

host,port = sys.argv[1].split(":")
port = int(port)
backlog = 5

def command(clients):
	while True:
		cmd = input('$')
		try:	host,cmd = cmd.split(':',1)
		except:	continue
		if host in clients:
			try:
				s = clients[host]
				s.send(cmd.encode())
				print(s.recv(1024).decode())
			except:
				print('failed')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
clients = {}
Thread(target=command, args=[clients]).start()
while True:
	sock,addx = s.accept()
	host = socket.gethostbyaddr(addx[0])[0]
	clients[host] = sock
	print('%s connected.' % host)

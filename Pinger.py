#!/usr/bin/env python

import socket


TCP_IP = '192.168.1.110'
TCP_PORT = 7777
BUFFER_SIZE = 1024
MESSAGE = input('Enter message: ')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(bytes(MESSAGE, 'utf-8'))
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data)

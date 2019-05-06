#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

connection, addr = s.accept()
print('Connection address:', addr)
while 1:
    data = connection.recv(BUFFER_SIZE)
    if not data: continue
    print("received data:",data)
    connection.send(bytes("Thanks chum.", 'utf-8'))  # echo
connection.close()
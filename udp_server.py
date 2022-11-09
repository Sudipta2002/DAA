# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 18:42:39 2022

@author: souvi
"""

import socket
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = ('localhost',10000)
server.bind(server_address)

data,address = server.recvfrom(1024)
print("Data:",data.decode())
data = data.upper()
server.sendto(data,address)
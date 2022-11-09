# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 18:42:52 2022

@author: souvi
"""

import socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = ('localhost',10000)

client.sendto("Hi server".encode(), server_address)

data,address = client.recvfrom(4096)
print("Got:",data.decode())
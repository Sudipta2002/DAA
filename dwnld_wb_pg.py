# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 07:36:43 2022

@author: souvi
"""

import socket
import sys
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("aurcc.ac.in",80))
s.sendall(b"GET /HTTP/1.0\r\nHost: www.aurcc.ac.in\r\nAccept:text/html\r\n\r\n")
print(str(s.recv(4096),'utf-8'))
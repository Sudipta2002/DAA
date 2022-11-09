import socket
import sys
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('localhost',10000)
server.bind(server_address)
server.listen(1)
connection,client_address = server.accept()




file_name = 'hello.txt'
connection.sendall(file_name.encode())
file = open('hello.txt','rb')
data = file.read()



connection.sendall(data)
file.close()
connection.close()
server.close()

import socket
import sys
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('localhost',10000)
server.bind(server_address)
server.listen(1)
print("Waiting for a connection...")
connection,client_address = server.accept()


print("Connnection Established:",client_address)
data = connection.recv(1024)
print("Received:",data.decode())

connection.sendall(data)
connection.close()
server.close()
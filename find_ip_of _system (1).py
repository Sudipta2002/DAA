# import socket
# hostname = socket.gethostname()
# IP = socket.gethostbyname(hostname)
# print("Computer name is: " + hostname)
# print("IP address of the system: " + IP)

import socket
hostname=socket.gethostname()
IP= socket.gethostbyname(hostname)
print(hostname)
print(IP)
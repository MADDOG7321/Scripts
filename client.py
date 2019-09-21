#TCP client for receiving files

from socket import *

HOST = "127.0.0.1"
PORT = 1024
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)
message = bytes(server.recv(4096)).decode("utf8")
data = message.split()
print(message)

filerequest = input("file to request: ")
while filerequest not in data[9:]:
    filerequest = input("file to request: ")

server.send(bytes(filerequest, "utf8"))

file = open(f"{filerequest}", 'wb')
while True:
    data = server.recv(32)
    if data:
        file.write(data)
    else:
        break

file.close()

#TCP server for sending files

from socket import *
from time import ctime
import os
import sys

class ClientHandler():
    def __init__(self, client, address):
        self.client = client
        self.address = address

    def run(self):
        print(f"sending {address} data...")

        options = os.listdir("files")
        data = ctime() + "\n What file you want?\n"
        for file in options:
            data += f"{file}\n"
            
        client.send(bytes(data, "utf8"))
        print("finished [1/2].")

        reply = client.recv(64).decode("utf8")
        print(f"sending file {reply}")
        file = open(f"files/{reply}", 'rb')
        filedata = b'' + file.read()
        print(sys.getsizeof(filedata))
        client.send(filedata)
        print("finished [2/2].")

        client.close()

HOST = "127.0.0.1"
PORT = 1024
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

while True:
    try:
        print("Waiting for connection...")
        client, address = server.accept()
        print(f"Connection from: {address}")
        
        handler = ClientHandler(client, address)
        handler.run()
    except KeyboardInterrupt:
        break

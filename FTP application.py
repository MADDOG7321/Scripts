#TCP server for sending files

from socket import *
from time import ctime
import os
import sys

passwd = "Password10"

SERVER_HOST = "127.0.0.1"

COMS_PORT = 4300
FILE_PORT = COMS_PORT + 1

def server():
    os.system("ipconfig > temp.txt")
    file = open("temp.txt", "r")
    strings = file.readlines()
    file.close()

    IPs = ["127.0.0.1",]
    for x in strings:
        findvar = x.find("IPv4 Address")
        if findvar > -1:
            IPs.append(x[x.find(":") + 2:].strip("\n"))
    
    IPstring = ""
    for ip in IPs:
        IPstring += ip + "\n"

    while True:      
        option = input("What IP address are you using for this action?\n" + IPstring)
        if option not in IPs:
            continue
        break

    SERVER_HOST = option

    COMS_ADDRESS = (SERVER_HOST, COMS_PORT)
    FILE_ADDRESS = (SERVER_HOST, FILE_PORT)
    
    coms_server = socket(AF_INET, SOCK_STREAM)
    coms_server.bind(COMS_ADDRESS)
    coms_server.listen(1)

    file_server = socket(AF_INET, SOCK_STREAM)
    file_server.bind(FILE_ADDRESS)
    file_server.listen(1)

    connections = input("How many connections do you wish to allow? (0 = infinite): ")

    writeLog(f"{ctime()} || ### STARTING SERVER ###\n{ctime()} || >Server bound to {COMS_ADDRESS}\n{ctime()} || >Listening...\n")
    while True:
        try:
            print(f"{ctime()} || Waiting for connection...")
            coms_client, coms_address = coms_server.accept()
            file_client, file_address = file_server.accept()
            writeLog(f"{ctime()} || Complete connection from: {coms_address}")

            while True:
                if client.recv(64).decode("utf-8") != passwd:
                    writeLog(f"Bad password from {coms_address}")
                    coms_client.close()
                    file_client.close()
                    break

                try:
                    filesindir = os.listdir("ShareFiles/")
                except:
                    print("{ctime()} || 'ShareFiles' directory not found. Creating directory")
                dirstring = ""
                for x in filesindir:
                    distring += x + "\n"
                
                requestfile = talkprotocol(coms_client, "What file are you requesting?\n" + dirstring, file)

                file = open("ShareFiles/" + requestfile, "rb")
                file_client.send(file.read())
                file.close()
                file_client.close()
                
        except KeyboardInterrupt:
            break
        
    print(f"{ctime()} || ### SERVER SHUTTING DOWN ###\n")

def talkprotocol(client, data, expectedReply):
    while True:
        client.send(bytes(data))
        reply = client.recv(4096).decode("utf-8")
        if reply != expectedReply or reply not in expectedReply:
            continue
        
        break
    return reply

def writeLog(entry):
    print(entry)
    file = open("Log.txt", "a")
    file.write(entry + "\n")
    file.close()

def client():
    SERVER_HOST = input("What is the server address? ")

    COMS_ADDRESS = (SERVER_HOST, COMS_PORT)
    FILE_ADDRESS = (SERVER_HOST, FILE_PORT)

    coms_server = socket(AF_INET, SOCK_STREAM)
    file_server = socket(AF_INET, SOCK_STREAM)

    coms_server.connect(COMS_ADDRESS)
    file_server.connect(FILE_ADDRESS)

    coms_server.send(bytes(input("Enter the password: ")))
    server.recv(4096
    

while True:
    option = input("1   Host connection.\n2   Join existing connection.\n3   Exit\n")
    if option == "1":
        server()
        continue
    elif option == "2":
        client()
        continue
    elif option == "3":
        break
    else:
        print("Error | Invalid input.")
        continue

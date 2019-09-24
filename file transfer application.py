from socket import *
from time import ctime
import os
import sys

passwd = "Password10"

SERVER = "127.0.0.1"
PORT = 4300

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
        option = input("What IP address are you using to host the server?\n" + IPstring)
        if option not in IPs:
            continue
        break

    SERVER = option

    ADDRESS = (SERVER, PORT)
    
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(ADDRESS)
    server.listen(1)

    writeLog(f"{ctime()} || ### STARTING SERVER ###\n{ctime()} || >Server bound to {ADDRESS}")
    while True:
        try:
            print(f"{ctime()} || Waiting for connection...")
            client, address = server.accept()
            
            writeLog(f"{ctime()} || Complete connection from: {address}")

            if client.recv(64).decode("utf-8") != passwd:
                writeLog(f"Bad password from {address}")
                client.close()
                continue

            while True:
                try:
                    filesindir = os.listdir("ShareFiles/")
                except:
                    print(f"{ctime()} || 'ShareFiles' directory not found. Creating directory")
                    os.mkdir("ShareFiles/")
                    filesindir = os.listdir("ShareFiles/")
                    
                dirstring = ""
                for x in filesindir:
                    distring += x + "\n"

                while True:
                    client.send(bytes("What file are you requesting?\n" + dirstring))
                    reply = lient.recv(4096).decode("utf-8")
                    if reply != "exit" or reply not in filesindir:
                        continue
                    break

                if reply == "exit":
                    writeLog(f"{ctime()} || Client {coms_address} disconnecting...")
                    client.close()
                    continue

                file = open("ShareFiles/" + reply, "rb")
                client.send(file.read())
                file.close()
                
        except KeyboardInterrupt:
            break
        
    print(f"{ctime()} || ### SERVER SHUTTING DOWN ###\n")

def writeLog(entry):
    print(entry)
    file = open("Log.txt", "a")
    file.write(entry + "\n")
    file.close()

def client():
    SERVER = input("What is the server address: ")
    ADDRESS = (SERVER, PORT)
    server = socket(AF_INET, SOCK_STREAM)
    server.connect(ADDRESS)

    server.send(bytes(input("Enter password: ")))
    reply = server.recv(4096).decode("utf-8")
    
    while True:
        requestfile = input("File to request: ")
        if requestfile not in reply:
            print("Error > no valid file entered")
            continue
        break

    file = open(requestfile, "wb")
    
    server.send(bytes(requestfile))

    while True:
        data = server.recv(1024)
        if data:
            file.write(data)
        else:
            break
    file.close()
    
    print("Finished downloading file")
        
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

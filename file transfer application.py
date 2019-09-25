from socket import *
from time import ctime
import os
import sys

passwd = "Password10"

SERVER = "127.0.0.1"
PORT = 4300

def server():
    iswindows = os.system("ipconfig > temp.txt")
    os.system("ifconfig > temp.txt")
    file = open("temp.txt", "r")
    strings = file.readlines()
    file.close()

    IPs = []
    if iswindows == 0:
        IPs.append("127.0.0.1")
        
    for x in strings:
        if iswindows == 0:
            findvar = x.find("IPv4 Address")
            if findvar > -1:
                IPs.append(x[x.find(":") + 2:].strip("\n"))
        else:
            findvar = x.find("inet ")
            if findvar > -1:
                IPs.append(x[x.find("inet ") + 5:x.find("netmask") - 2])

    print(IPs)
    
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
                writeLog(f"{ctime()} || Bad password from {address}")
                client.close()
                continue
            
            try:
                filesindir = os.listdir("ShareFiles/")
            except:
                print(f"{ctime()} || 'ShareFiles' directory not found. Creating directory")
                os.mkdir("ShareFiles/")
                filesindir = os.listdir("ShareFiles/")
                    
            dirstring = ""
            for x in filesindir:
                dirstring += x + "\n"

            client.send(bytes("What file are you requesting?\n" + dirstring, "utf-8"))
            reply = client.recv(4096).decode("utf-8")

            file = open("ShareFiles/" + reply, "rb")
            client.send(file.read())
            file.close()
            client.close()
            writeLog(f"{ctime()} || Sent {reply} to {address}\n{ctime()} || Disconnecting client")

        except ConnectionResetError:
            writeLog(f"{ctime()} || Connection was lost")
            continue
         
        except KeyboardInterrupt:
            break
        
    print(f"{ctime()} || ### SERVER SHUTTING DOWN ###\n")

def writeLog(entry):
    print(entry)
    file = open("Log.txt", "a")
    file.write(entry + "\n")
    file.close()

def client():
    try:
        SERVER = input("What is the server address: ")
        ADDRESS = (SERVER, PORT)
        server = socket(AF_INET, SOCK_STREAM)
        server.connect(ADDRESS)

        server.send(bytes(input("Enter password: "), "utf-8"))
        reply = server.recv(4096).decode("utf-8")
        reply = reply[:-1]
        print(reply)

        fileschoice = reply.split("\n")
        print(fileschoice)
        
        while True:
            requestfile = input("File to request: ")
            if requestfile not in fileschoice:
                print("Error > no valid file entered")
                continue
            try:
                file = open(requestfile, "wb")
            except FileNotFoundError:
                print("Error > no valid file entered")
                continue
            break

        file = open(requestfile, "wb")
    
        server.send(bytes(requestfile, "utf-8"))

        while True:
            data = server.recv(1024)
            if data:
                file.write(data)
            else:
                break
        file.close()
    
        print("Finished downloading file\n\n")

    except ConnectionResetError:
        print(f"{ctime()} || Connection was lost")
        
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

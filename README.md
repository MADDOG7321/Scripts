# Scripts
## 'IP to binary.py'
Converts IP addresses to binary.
NOTE: input must be formatted correctly and be a valid ip address eg. 0.0.0.0 -> 255.255.255.255

## 'client.py'
TCP client for receiving files

## 'downloadfile.py'
Simple function that can download files from a website. When running the script on its own, the program will access a 'urls.txt' file and read entries to be downloaded and removes the entry from the list when finished downloading that item.

## 'file transfer application.py'
A file server and client application that can serve or receive files. 

## 'ping logger for domain computers.ps1'
A very basic powershell script for logging pings to an IP or domain name. Designed to be run on multiple hosts from a server.

## 'server.py'
TCP server for sending files

## 'wolf class example.py'
Random python script playing around with classes in python. In this script a pre-defined area is made and with each 'wolf' object made will automatically be assigned a random coordinate in the area and write a W in the map representing a wolf. The 'wolf' class has a few functions:
* **getPos(self) -** returns the objects current coordinates.
* **changePos(self, x, y) -** Assigns the wolf's new and removes the wolf's old position from the map (if no other wolf shares the previous coordinate), then positions the wolf's new coordinate on the map.
* **randmove(self) -** chooses a random direction (up, down, left, or right), checks if the position is still within the bounds of the area. If the direction is within the bounds the object will take it's current position and increment/decrement accordingly in the afforementioned direction, else the function will restart.

Other functions include:
* **isCoordDuplicate(selfwolf) -** Checks if the coordinate is shared with another wolf object.
* **printMap() -** Prints the map.

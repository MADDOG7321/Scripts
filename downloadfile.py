#Simple function that can download file links from a website. When running the script on its own, the program will access a 'urls.txt' file and read entries to be downloaded and removes the entry from the list when complete.

import urllib.request
import time

def downloadUrlFile(fileurl):
    fileurl = fileurl.strip("\n") #Remove newline characters from the end of lines
    print(f"{time.ctime()} || Sending request to: {fileurl}")
    req = urllib.request.Request(fileurl, headers={'User-Agent': 'Mozilla/5.0'}) #Define url request
    reply = urllib.request.urlopen(req) #Open the url with the request

    filename = fileurl[fileurl.rfind('/') + 1:] #Get the filename from the url
    print(f"{time.ctime()} || Writing to file {filename}")
    file = open(filename, 'wb') #Create file
    file.write(reply.read()) #Write to file
    file.close()

    print(f"{time.ctime()} || Finished downloading {filename}")

if __name__ == "__main__": #Independent code when not used as a library
    while True:
        try:
            file = open("urls.txt", "r") #Try open the file
        except FileNotFoundError:
            file = open("urls.txt", "x") #Create the file if it doesn't exist
            file.close()
            continue
        
        urls = file.readlines()
        file.close()
        
        if len(urls) < 1: #Check if the file has
            break
        
        downloadUrlFile(urls[0])

        file = open("urls.txt", "w")
        file.writelines(urls[1:]) #Remove first line from entries
        file.close()

    print(f"{time.ctime()} || List is now empty")
    input("Press any key to exit...")


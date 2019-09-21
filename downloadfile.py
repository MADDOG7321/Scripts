#Simple function that can download file links from a website. When running the script on its own, the program will access a 
#   'urls.txt' file and read entries to be downloaded and removes the entry from the list when complete.

import urllib.request
import time

def downloadUrlFile(fileurl):
    fileurl = fileurl.strip("\n\r")
    print(f"{time.ctime()} || Sending request to: {fileurl}")
    req = urllib.request.Request(fileurl, headers={'User-Agent': 'Mozilla/5.0'})
    reply = urllib.request.urlopen(req)

    filename = fileurl[fileurl.rfind('/') + 1:]
    print(f"{time.ctime()} || Writing to file {filename}")
    file = open(filename, 'wb')
    file.write(reply.read())
    file.close()

    print(f"{time.ctime()} || Finished downloading {filename}")

if __name__ == "__main__":
    while True:
        try:
            file = open("urls.txt", "r")
        except FileNotFoundError:
            file = open("urls.txt", "x")
            file.close()
            continue
        
        urls = file.readlines()
        file.close()
        
        if len(urls) < 1:
            break
        
        downloadUrlFile(urls[0])

        file = open("urls.txt", "w")
        file.writelines(urls[1:])
        file.close()

    print(f"{time.ctime()} || List is now empty")
    input("Press any key to exit...")


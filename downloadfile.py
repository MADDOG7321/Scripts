import urllib.request
import time

def downloadfile(fileurl):
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
    file = open("urls.txt", "r")
    urls = file.readlines()
    file.close()

    for url in urls:
        downloadfile(url)

import socket

url = input("Enter a URL: ")
host = url.split("/")[2]

try:
  mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  mysock.connect((host, 80))
  cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
  mysock.send(cmd)
except:
  print("URL could not be opened:", url)
  exit()

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

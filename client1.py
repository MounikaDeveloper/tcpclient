import socket
PORT=5050
#HOST =socket.gethostbyname(socket.gethostname())
HOST='172.18.144.2'
client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
client.connect((HOST,PORT))
#print(c.rev(1024).decode())


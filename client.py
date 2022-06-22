import socket

client = socket.socket()

name = input('Input your name: ')
client.connect(('127.0.0.1', 9090))
client.send(name.encode())

server_name = client.recv(1024).decode()
print(server_name, ' connected!')

while True:
    message = (client.recv(1024)).decode()
    print(server_name, ':', message)
    message = input('Me: ')
    client.send(message.encode())
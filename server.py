import socket

server = socket.socket()
server.bind(('127.0.0.1', 9090))
server.listen()

print("server started...")

name = input('Input your name:')
conn, addr = server.accept()

client_name = (conn.recv(1024)).decode()
print(client_name + ' connected!')
conn.send(name.encode())

while True:
    message = input('Me: ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client_name, ':', message)

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 1337))
client_socket.send(b"Do you want to play a game?\n")
received = client_socket.recv(1024)
print(received)
client_socket.close()
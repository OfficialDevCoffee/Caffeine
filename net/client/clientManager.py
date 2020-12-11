from socket import *

#DEF Host & Port
HOST = '127.0.0.1'
PORT = 8009

#DEF a socket to Connect with server.
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((HOST, PORT))

message = clientSocket.recv(1024)
print(message.decode('utf-8'))
buffer = input()
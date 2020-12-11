from socket import *

#DEF Host & Port
HOST = ''
PORT = 8009

#DEF Use of Socket, AF_INET points ipv4 connections.
serverSocket = socket(AF_INET, SOCK_STREAM)
#Bind must be declared, especially on broadcasting(server).
serverSocket.bind((HOST, PORT))
#listen(max_accepted_connections)
serverSocket.listen(1)

#socket.accept() function remains until client is connected with.
connectionSocket, address = serverSocket.accept()
print(address)

message = 'Hello World'
connectionSocket.send(message.encode('utf-8'))
buffer = input()
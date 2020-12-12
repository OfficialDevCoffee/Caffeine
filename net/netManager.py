from socket import *
import time, threading

class serverManager:

    serverSocket = socket(AF_INET, SOCK_STREAM)
    fileSocket = socket(AF_INET, SOCK_STREAM)
    HOST = ''
    SERVER_PORT = 9010
    FILE_PORT = 9011
    MAX_CONNECTION = 1
    CONNECTION_NUMBER = 0

    sendService = None
    recieveService = None

    userList = {}

    def listen_server(self, serverSocket):
        connectionSocket, address = serverSocket.accept()
        self.CONNECTION_NUMBER += 1
        print('[Log In Event] ' + print)
    def start_listen(self):
        self.serverSocket.bind((self.HOST, self.PORT))
        self.serverSocket.listen(self.MAX_CONNECTION)
        self.connectionSocket, self.address = self.serverSocket.accept()
        self.CONNECTION_NUMBER += 1
        print(str(self.address) + ' 접속. 총 클라이언트 수: ' + str(self.CONNECTION_NUMBER))
        pass

    def send(self, connectionSocket):
        while True:
            message = input('>> ')
            connectionSocket.send(message.encode('utf-8'))
            pass
        pass

    def recieve(self, connectionSocket):
        while True:
            message = connectionSocket.recv(1024).decode('utf-8')
            print('Counter: ' + str(message))
            pass
        pass

    def start_service(self):
        self.sendService = threading.Thread(target = self.send, args = (self.connectionSocket,))
        self.recieveService = threading.Thread(target =  self.recieve, args = (self.connectionSocket,))
        self.sendService.start()
        self.recieveService.start()
        pass
    
    def start_waiting(self):
        while True:
            time.sleep(1)
            pass
        pass

    def __init__(self, HOST = '', PORT = 9010, MAX_CONNECTION = 1):
        self.HOST = HOST
        self.PORT = PORT
        self.is_connected = False
        pass

    pass

class clientManager:

    clientSocket = socket(AF_INET, SOCK_STREAM)
    HOST = 'localhost'
    PORT = 9010

    is_connected = False

    sendService = None
    recieveService = None
        
    def start_listen(self):
        self.clientSocket.connect((self.HOST, self.PORT))
        self.is_connected = True
        print(self.HOST + " 접속됨.")
        pass
    
    def send(self, clientSocket):
        while True:
            message = input('>> ')
            clientSocket.send(message.encode('utf-8'))
            pass
        pass

    def recieve(self, clientSocket):
        while True:
            message = clientSocket.recv(1024).decode('utf-8')
            print('Counter: ' + str(message))
            pass
        pass

    def start_service(self):
        self.sendService = threading.Thread(target = self.send, args = (self.clientSocket,))
        self.recieveService = threading.Thread(target = self.recieve, args = (self.clientSocket,))
        self.sendService.start()
        self.recieveService.start()
        pass

    def start_waiting(self):
        while True:
            time.sleep(1)
            pass
        pass

    def __init__(self, HOST = 'localhost', PORT = 9010):
        self.HOST = HOST
        self.PORT = PORT
        self.is_connected = False
        pass

    pass

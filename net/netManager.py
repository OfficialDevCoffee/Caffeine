# netManager.py
# Created On 2021-02-04, by dev. Coffee Official
# For more information or to contact, please email to this address: official.devcoffee@gmail.com

import socket, threading, time

class ServerManager():
    SERVER_PORT = 9009
    Server_Socket = None
    
    def __init__(self, server_port= 9009):

        self.SERVER_PORT = server_port

        self.Server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Server_Socket.bind(('', self.SERVER_PORT))
        self.Server_Socket.listen()
        self.log("Server Started At / SERVER_PORT: " + str(self.SERVER_PORT))

        try:
            while True:
                client_socket, client_address = self.Server_Socket.accept()
                client_thread = threading.Thread(target= self.bind, args= (client_socket, client_address))
                client_thread.start()
                pass
        except:
            self.log("Server Internal Error. Shutting Down.")
            pass
        finally:
            self.Server_Socket.close()
            pass
        pass

    def log(self, message):
        now = time.localtime()
        timestamp = "[%04d-%02d-%02d %02d:%02d:%02d INFO]" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        print(timestamp, message)
        pass

    def bind(self, client_socket, client_address):
        self.log("Client Connected >> " + str(client_address))
        try:
            # 접속 종료시 except 나옴.
            while True:
                data = client_socket.recv(4)
                incoming_bytes_length = int.from_bytes(data, "little")
                data = client_socket.recv(incoming_bytes_length).decode()
                self.log("Client Issued To Send Message >> Client Address: " + str(client_address) + ", Message: " + str(data))
                pass
        except:
            self.log("Client Disconnected >> " + str(client_address))
            pass
        finally:
            client_socket.close()
            pass
        pass
    pass

class ClientManager():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 9009
    Client_Socket = None

    def __init__(self, server_host= '127.0.0.1', server_port= 9009):
        self.SERVER_HOST = server_host
        self.SERVER_PORT = server_port

        self.Client_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Client_Socket.connect((self.SERVER_HOST, self.SERVER_PORT))

        recvThread = threading.Thread(target= self.recv, args= (self.Client_Socket,))
        recvThread.start()
        pass

    def send(self, data):
        raw_data = data.encode()
        data_bytes_length = len(raw_data)
        
        try:
            # server로 데이터 길이를 전송
            self.Client_Socket.sendall(data_bytes_length.to_bytes(4, byteorder="little"))
            # server로 raw_data 전송
            self.Client_Socket.sendall(raw_data)
            pass
        except:
            self.Client_Socket.close()
            pass
        pass

    def recv(self, client_socket):
        try:
            # 접속 종료시 except 나옴.
            while True:
                incoming_bytes_length = int.from_bytes(client_socket.recv(4), "little")
                data = client_socket.recv(incoming_bytes_length).decode()
                self.dataHandle()
                pass
        except:
            pass
        finally:
            client_socket.close()
            pass
        pass
    pass

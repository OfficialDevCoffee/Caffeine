# clientManager.py
# Created On 2021-02-04, by dev. Coffee Official
# For more information or to contact, please email to this address: official.devcoffee@gmail.com

import socket, threading

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

'''
if __name__ == '__main__':
    clientManager = ClientManager()
    clientManager.send('Hello')
    pass
'''
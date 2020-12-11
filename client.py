from net.netManager import clientManager

HOST = 'localhost'
PORT = 9010
manager = clientManager(HOST, PORT)
manager.start_listen()
manager.start_service()

manager.start_waiting()
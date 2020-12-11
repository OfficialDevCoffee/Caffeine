from net.netManager import serverManager

HOST = ''
PORT = 9010
MAX_CONNECTION = 1
manager = serverManager(HOST, PORT, MAX_CONNECTION)
manager.start_listen()
manager.start_service()

manager.start_waiting()
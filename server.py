import socket, time
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8000))
server.listen(2)

client_1, addres_1 = server.accept()
client_2, addres_2 = server.accept()

def send1():
    while True:
        data_1 = client_1.recv(2048)
        client_2.sendall(data_1)

def send2():
    while True:
        data_2 = client_2.recv(2048)
        client_1.sendall(data_2)


threading.Thread(target=send1).start()
threading.Thread(target=send2).start()

while True:
    time.sleep(1)


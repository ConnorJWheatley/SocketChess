import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = str(socket.gethostname())
        self.port = 5555
        self.address = (self.server, self.port)
        self.player_num = int(self.connect())

    # attempt to connect to the server to start sending data
    def connect(self):
        try:
            self.client.connect(self.address)
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

    # sending data to the server
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)
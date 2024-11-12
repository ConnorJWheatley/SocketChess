import socket
import pickle
from _thread import start_new_thread
from game.game_state import GameState

class Server:
    def __init__(self):
        self.games = {}
        self.id_count = 0

    @property
    def games(self):
        return self._games

    @games.setter
    def games(self, games):
        self._games = games

    @property
    def id_count(self):
        return self._id_count

    @id_count.setter
    def id_count(self, id_count):
        self._id_count = id_count

    def threaded_client(self, client_conn, player, game_id):
        client_conn.sendall(str(player).encode()) # sends the player number to the client
        print(f"Player number {player} has joined on game_id {game_id}")

        reply = ""
        while True:
            try:
                # receive message from client
                # either "get_board" or making a move
                data = client_conn.recv(4096).decode()

                # making sure the game still exists - if client disconnects then we delete the game
                if game_id in self.games:
                    game = self.games[game_id]

                    if not data:
                        print(f"Player number {player} has disconnected on game_id {game_id}")
                        break

                    else:
                        if data == "get_game_state":
                            game_state = game.send_game_state()
                            client_conn.sendall(pickle.dumps(game_state))

                else:
                    break

            except socket.error as e:
                print(e)
                break

        self.id_count -= 1
        client_conn.close()

    def server_loop(self):
        # used to get server IP address rather than hard coding
        hostname = socket.gethostname()
        port = 5555
        server_address = (hostname, port)
        ip_addr = str(socket.gethostbyname(hostname))

        print(f"Server started on {ip_addr}:{port}. Waiting for connection...")

        # get instance of server socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind host address and port together
        try:
            server_socket.bind(server_address)
        except socket.error as e:
            print(str(e))

        # configure how many clients the server can listen to simultaneously
        # 2 for now
        server_socket.listen(2)

        while True:
            # accept new connection
            conn, address = server_socket.accept()
            print(f"Connection from: {address}")

            self.id_count += 1
            player = 1
            game_id = (self.id_count - 1) // 2

            # check to see if a new game needs to be created
            if self.id_count % 2 == 1:
                self.games[game_id] = GameState(game_id)
                print(f"Creating a new game with ID: [{game_id}]")
            else:
                self.games[game_id].ready = True
                player = 2

            start_new_thread(self.threaded_client, (conn, player, game_id))

if __name__ == "__main__":
    server = Server()
    server.server_loop()
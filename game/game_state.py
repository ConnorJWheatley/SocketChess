from game.board import Board

class GameState:
    def __init__(self, game_id):
        self.id = game_id
        self.ready = False
        # self.board = Board(1000, 1000)
        self.player_turn = "white"

        # could maybe invert this when making the board for whoever is playing black
        self.game_state = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]

    def send_game_state(self):
        return self.game_state

    def update_board(self):
        pass
        # move from client
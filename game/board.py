from game.square import Square
from game.pieces.Bishop import Bishop
from game.pieces.King import King
from game.pieces.Knight import Knight
from game.pieces.Pawn import Pawn
from game.pieces.Queen import Queen
from game.pieces.Rook import Rook


class Board:
    def __init__(self, width, height, player_num, game_state):
        """
        Create a new Board object with the given width and height.

        The width and height are used to calculate the size of each square.
        The squares are created and stored in the `squares` field.
        The `config` field is set to the default configuration for a chess board.
        The `setup_pieces` method is called to place the pieces on the squares.

        :param width: The width of the board in pixels
        :param height: The height of the board in pixels
        """
        self.width = width
        self.height = height
        self.sqr_width = width // 8
        self.sqr_height = height // 8
        self.squares = self.create_squares()
        self.player_num = player_num
        self.game_state = game_state
        self.setup_pieces()

    def create_squares(self):
        all_squares = []
        for x in range(8):
            for y in range(8):
                # Create a Square object for each position on the 8x8 board
                all_squares.append(
                    Square(x, y, self.sqr_width, self.sqr_height,
                           (75, 75, 75),
                           (255, 255, 255),
                           (0, 255, 0)
                    )
                )
        return all_squares

    def draw_board(self, window):
        for square in self.squares:
            square.draw(window)

    def get_square_from_pos(self, pos):
        # Given a pos (x, y) in grid coordinates, return the square object at that position.
        for square in self.squares:
            if (square.x, square.y) == (pos[0], pos[1]):
                return square

    def get_piece_from_pos(self, pos):
        return self.get_square_from_pos(pos).piece

    def setup_pieces(self):
        # mapping of piece type to class
        piece_classes = {
            'Q': Queen,
            'K': King,
            'R': Rook,
            'B': Bishop,
            'N': Knight,
            'P': Pawn
        }

        initial_game_state = None
        if self.player_num != 1:
            initial_game_state = self.game_state[::-1]
            initial_game_state[0] = initial_game_state[0][::-1]
            initial_game_state[7] = initial_game_state[7][::-1]
        else:
            initial_game_state = self.game_state

        # loop through the config and place pieces on squares
        # y is the row and x is the column
        for y, row in enumerate(initial_game_state):
            for x, piece_code in enumerate(row):
                if piece_code:
                    square = self.get_square_from_pos((x, y))

                    # get the type of piece e.g 'Q' for queen, and its colour
                    piece_type = piece_code[1]
                    colour = 'white' if piece_code[0] == 'w' else 'black'

                    # get the class for the type of piece
                    piece_class = piece_classes.get(piece_type)
                    if piece_class:
                        square.piece = piece_class((x, y), colour)
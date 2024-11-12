from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, pos, colour):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.colour = colour
        self.has_moved = False

    @abstractmethod
    def get_legal_moves(self):
        ...

    @abstractmethod
    def get_pos(self, board):
        ...

    @abstractmethod
    def make_move(self, board):
        ...
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

    @staticmethod
    def resize_img(img):
        scale_factor = 0.85  # 50% of the original size
        new_size = (int(img.get_width() * scale_factor), int(img.get_height() * scale_factor))
        return new_size
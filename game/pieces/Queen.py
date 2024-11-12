from game.piece import Piece
import pygame

class Queen(Piece):
    def __init__(self, pos, colour):
        super().__init__(pos, colour)
        img_path = f"..\\images\\{colour}-queen.png"
        self.img = pygame.image.load(img_path).convert_alpha()

    # finds what moves are possible from the piece's current position
    def get_legal_moves(self):
        print(f"I am a QUEEN")

    def get_pos(self, board):
        print(f"I am at this position: {self.pos}")

    def make_move(self, board):
        print("I am making a move")
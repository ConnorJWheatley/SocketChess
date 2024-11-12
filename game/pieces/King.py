from game.piece import Piece
import pygame

class King(Piece):
    def __init__(self, pos, colour):
        super().__init__(pos, colour)
        img_path = f"..\\images\\{colour}-king.png"
        self.img = pygame.image.load(img_path).convert_alpha()

    # finds what moves are possible from the piece's current position
    def get_legal_moves(self):
        print("I am a King")

    def get_pos(self, board):
        print("I am at this position")

    def make_move(self, board):
        print("I am making a move")
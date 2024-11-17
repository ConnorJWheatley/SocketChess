from game.piece import Piece
import pygame

class Pawn(Piece):
    def __init__(self, pos, colour):
        super().__init__(pos, colour)
        img_path = f"..\\images\\{colour}-pawn.png"
        self.img = pygame.image.load(img_path).convert_alpha()

        # scales the piece's image - makes room to place number and letter for square
        new_size = self.resize_img(self.img)
        self.img = pygame.transform.scale(self.img, new_size)

    # finds what moves are possible from the piece's current position
    def get_legal_moves(self):
        print("I am a pawn")

    # gets the position of the piece on the board
    def get_pos(self, board):
        print("I am at this position")

    def make_move(self, board):
        print("I am making a move")
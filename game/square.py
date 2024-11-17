import pygame

class Square:
    def __init__(self, x, y, width, height, dark_colour, light_colour, highlight_colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.abs_x = x * width
        self.abs_y = y * height
        self.pos = (x, y)
        self.abs_pos = (self.abs_x, self.abs_y)
        self.colour = "light" if (x + y) % 2 == 0 else "dark"
        self.draw_colour = dark_colour if self.colour == "dark" else light_colour
        self.highlight = False
        self.highlight_colour = highlight_colour
        self.piece = None
        self.rect = pygame.Rect(
            self.abs_x,
            self.abs_y,
            self.width,
            self.height
        )
        self.rank_and_file = self.get_sqr_name()

    def get_sqr_name(self):
        files = "abcdefgh"
        return files[self.x] + str(self.y + 1)

    def draw(self, window):
        if self.highlight:
            pygame.draw.rect(window, self.highlight_colour, self.rect)
        else:
            pygame.draw.rect(window, self.draw_colour, self.rect)

        if self.piece is not None:
            # centers the piece in the square
            piece_center_rect = self.piece.img.get_rect()
            piece_center_rect.center = self.rect.center
            window.blit(self.piece.img, piece_center_rect.topleft)
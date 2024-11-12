# import pygame
# from game.board import Board
# from game.game_state import GameState
#
# # pygame setup
# win_width = 1000
# win_height = 1000
# pygame.display.set_caption("Testing")
#
# def main():
#     pygame.init()
#     window = pygame.display.set_mode((win_width, win_height))
#     running = True
#     clock = pygame.time.Clock()
#
#     game_state = GameState(1)
#
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#                 pygame.quit()
#
#         # render game here
#         game_state.board.draw_board(window)
#
#         pygame.display.update()
#
#         clock.tick(60)
#
# main()

a = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]

print(f"Here is the original game state: {a}")
print(f"Here is the game state flipped: {a[::-1]}")
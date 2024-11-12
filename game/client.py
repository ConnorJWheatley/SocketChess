from game.board import Board
import pygame
from game.network import Network

win_width = 1000
win_height = 1000
pygame.display.set_caption("Connor\'s Chess")

def draw_board(window, board, new_game_state):
    board.game_state = new_game_state

    for square in board.squares:
        square.draw(window)

def main():
    # pygame setup

    pygame.init()
    window = pygame.display.set_mode((win_width, win_height))
    running = True
    clock = pygame.time.Clock()

    # The class that handles the communication with the server
    net = Network()

    # grabbing the initial game state
    game_state = net.send("get_game_state")
    board = Board(win_width, win_height, net.player_num, game_state)
    draw_board(window, board, game_state)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        current_game_state = None
        try:
            # got to be a better way i.e. just listen and only update when server sends update
            current_game_state = net.send("get_game_state")
        except (ConnectionResetError, ConnectionAbortedError):
            print("Lost connection to the server")
            running = False

        # will only re-render the game if the game state has changed, preventing unnecessary rendering
        if current_game_state != board.game_state:
            draw_board(window, board, current_game_state)

        pygame.display.update()

        clock.tick(60)

main()
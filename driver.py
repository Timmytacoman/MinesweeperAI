import globals
import board
import tile
import os
import pygame
import argparse
import numpy as np

# set the pygame window name
pygame.display.set_caption('Minesweeper AI')


def print_tiles():
    for row in globals.list_of_tiles:
        for current_tile in row:
            print(current_tile)


def init_parser():
    # instantiate the parser
    parser = argparse.ArgumentParser(description='Specify game parameters')
    # add arguments for rows and cols
    parser.add_argument('--size', type=int, help="Enter the size of the board to generate")
    # collect input size if present
    input_size = parser.parse_args().size
    if input_size is not None:
        globals.size = input_size


def init_board():
    print(f"size = {globals.size}")

    # init pygame
    pygame.init()

    # construct the game window
    window_length = globals.size * globals.size_scale
    print(f"window_length = {window_length}")
    globals.screen = pygame.display.set_mode([window_length, window_length])

    # from board.py
    board.setup_board()


def game_loop():
    # Run until the user asks to quit
    running = True

    while running:

        # Draws the surface object to the screen.
        pygame.display.update()

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # on mouse click
            if event.type == pygame.MOUSEBUTTONUP:
                click_type = event.button

                # left click
                if click_type == 1:
                    pass

                # right click
                if click_type == 3:
                    pass

    # Quit
    pygame.quit()


def play_game():
    init_parser()
    init_board()
    game_loop()


if __name__ == '__main__':
    play_game()

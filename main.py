import numpy
import pygame
import argparse

# default board edge size
defaultEdgeSize = 20

# instantiate the parser
parser = argparse.ArgumentParser(description='Specify game parameters')

# add arguments for rows and cols
# TODO add screensize argument
parser.add_argument('--size', type=int, default=defaultEdgeSize, help="enter the size of the board to generate")

# collect input size
args = parser.parse_args()
size = args.size

# screen dimensions
screenSize = size * 30

print(f"Generating board size: {size}")
print(f"Screen size: {screenSize}")

# init the pygame library
pygame.init()

# determine tile length
tileLength = screenSize / size
print(f"tileLength = {tileLength}")

# Set up the drawing window
screen = pygame.display.set_mode([screenSize, screenSize])

# global list of all the tile objects
listOfTiles = []


class Tile:
    def __init__(self, x, y, color):
        # x and y denote the top left position of the tile
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        # this is called when you print a Tile object
        return str(f"x={self.x}\ny={self.y}\ncolor={self.color}")


def init_board():
    # initialize the board

    # fill the screen white
    screen.fill((255, 255, 255))

    # construct all the tiles
    for row in range(size):
        for col in range(size):
            # construct tile obj
            x = col * tileLength
            y = row * tileLength
            color = (100, 100, 100)
            print(Tile(x, y, color))

            # pygame.rect obj takes (left, top, width, height)
            # pygame.draw.rect(screen, tileBorderColor,
            #                  pygame.Rect(col * tileLength, row * tileLength, tileLength, tileLength), 2)

    pygame.display.flip()


# initialize the board
init_board()

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # on mouse click
        if event.type == pygame.MOUSEBUTTONUP:
            # declare position
            xClick, yClick = pygame.mouse.get_pos()

            print(xClick, yClick)

# Done! Time to quit.
print("Goodbye!")
pygame.quit()

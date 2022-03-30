import pygame
import argparse
import random

# default board edge size
defaultEdgeSize = 20

# instantiate the parser
parser = argparse.ArgumentParser(description='Specify game parameters')

# add arguments for rows and cols
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

# set the pygame window name
pygame.display.set_caption('Minesweeper AI')

# determine tile length
tileLength = screenSize / size
print(f"tileLength = {tileLength}")

# Set up the drawing window
screen = pygame.display.set_mode([screenSize, screenSize])

# global list of all the tile objects
listOfTiles = []


def getScaledImage(name):
    # returns the scaled image of the desired image
    return pygame.transform.scale(pygame.image.load(f"./assets/{name}.png"), (tileLength, tileLength))


# image constructing
tileImage = getScaledImage('tile')
emptyImage = getScaledImage('empty')


class Tile:
    def __init__(self, x, y, image=None):
        # x and y denote the top left position of the tile
        self.x = x
        self.y = y
        self.image = image

    def __str__(self):
        # this is called when you print a Tile object
        return str(f"x={self.x}\ny={self.y}")

    def setImage(self, image):
        self.image = image


def init_board():
    # initialize the board

    # construct all the tiles
    for row in range(size):
        for col in range(size):
            # construct tile obj
            x = col * tileLength
            y = row * tileLength
            # create the tile
            newTile = Tile(x, y, tileImage)
            # append it to list
            listOfTiles.append(newTile)
            # draw tiles
            screen.blit(tileImage, (x, y))

    pygame.display.flip()


def draw_board():
    for tile in listOfTiles:
        screen.blit(tile.image, (tile.x, tile.y))
    pygame.display.flip()


def on_click(x, y):
    nearestTile = None
    shortest = tileLength
    # determine what tile was closest
    for tile in listOfTiles:
        # distance formula
        xDistance = abs(tile.x + (tileLength / 2) - x)
        yDistance = abs(tile.y + (tileLength / 2) - y)
        distance = xDistance + yDistance
        if distance < shortest:
            shortest = distance
            nearestTile = tile
    # get new image
    nearestTile.setImage(emptyImage)
    print(f"nearestTile = \n{nearestTile}")


# initialize the board
init_board()

# Run until the user asks to quit
running = True
while running:

    draw_board()

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # on mouse click
        if event.type == pygame.MOUSEBUTTONUP:
            # declare position
            xClick, yClick = pygame.mouse.get_pos()
            on_click(xClick, yClick)

# Done! Time to quit.
print("Goodbye!")
pygame.quit()

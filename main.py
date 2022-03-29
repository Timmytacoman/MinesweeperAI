import numpy
import pygame
import argparse

# instantiate the parser
parser = argparse.ArgumentParser(description='Specify board dimensions')

# add arguments for rows and cols
parser.add_argument('rows')
parser.add_argument('cols')

# collect input rows and cols
args = parser.parse_args()
rows = args.rows
cols = args.cols

# init the pygame library
pygame.init()

# params for grid dimensions m x n
m = 5
n = 5

# setup the grid
grid = numpy.zeros((m, n))

# Set up the drawing window
screen = pygame.display.set_mode([750, 750])


def draw():
    # draw tiles

    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()


# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    draw()

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
print("Goodbye!")
pygame.quit()

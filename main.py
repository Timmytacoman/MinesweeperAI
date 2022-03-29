import numpy
import pygame
import argparse

# default board size
defaultRows = 10
defaultCols = 10

# instantiate the parser
parser = argparse.ArgumentParser(description='Specify game parameters')

# add arguments for rows and cols
parser.add_argument('--rows', default=defaultRows, help="enter number of rows to be generated")
parser.add_argument('--cols', default=defaultCols, help="enter number of columns to be generated")

# collect input rows and cols
args = parser.parse_args()
rows = args.rows
cols = args.cols

print(f"Generating board size: {rows} x {cols}")
exit()

# init the pygame library
pygame.init()

# setup the grid
grid = numpy.zeros((rows, cols))

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

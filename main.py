import numpy
import pygame

pygame.init()

# params for grid dimensions m x n
m = 5
n = 5

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
pygame.quit()

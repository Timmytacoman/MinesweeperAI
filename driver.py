import pygame
import argparse


def setup():
    # instantiate the parser
    parser = argparse.ArgumentParser(description='Specify game parameters')



def game_loop():
    # init pygame
    pygame.init()

    # Run until the user asks to quit
    running = True

    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # on mouse click
            if event.type == pygame.MOUSEBUTTONUP:
                click_type = event.button
                print(click_type)
                x_click, y_click = pygame.mouse.get_pos()

                # left click
                if click_type == 1:
                    pass

                # right click
                if click_type == 3:
                    pass

    # Quit
    pygame.quit()


game_loop()
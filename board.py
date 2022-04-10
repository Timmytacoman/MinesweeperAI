import os
import driver
import tile
import globals
import pygame


def count_surrounding_tiles():
    print("Beginning counting surrounding tiles")

    # for every tile
    for row in globals.list_of_tiles:
        for current_tile in row:
            # var to hold bomb count
            bomb_count = 0
            # determine neighbors
            for x in range(-1, 2):
                for y in range(-1, 2):
                    col_to_check = current_tile.col + x
                    row_to_check = current_tile.row + y
                    try:
                        tile_to_check = globals.list_of_tiles[row_to_check][col_to_check]
                        # increment bomb count if it is a bomb
                        if tile_to_check.is_bomb is True:
                            bomb_count += 1
                    except IndexError:
                        # this occurs when the tile we are checking is out of bounds
                        pass
            # add bomb_count to tile obj
            current_tile.set_bomb_count(bomb_count)

    print("Finishing counting surrounding tiles")


def setup_board():
    # construct all tiles with chance of bomb
    tile.construct_tiles()
    # determine surrounding bomb counts
    count_surrounding_tiles()
    # display blank board
    draw_board()


def draw_board():
    print("Beginning draw_board")

    # create a surface object, image is drawn on it.
    image = pygame.image.load(r'assets/tile.png')

    for row in globals.list_of_tiles:
        for current_tile in row:
            print(current_tile)
            globals.screen.blit(image, (0, 0))

    print("Finish draw_board")


if __name__ == '__main__':
    # configure assets
    list_of_assets = os.listdir(os.getcwd() + "/assets")
    for i in list_of_assets:
        print(i)

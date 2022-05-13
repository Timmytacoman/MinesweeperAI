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
                    print(col_to_check)
                    print(row_to_check)
                    # ensure that we don't check negative a negative col or row, because
                    # numpy wraps to the end of array
                    if col_to_check < 0 or row_to_check < 0:
                        continue
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
    globals.screen.fill((185, 185, 185))
    # construct all tiles with chance of bomb
    tile.construct_tiles()
    # determine surrounding bomb counts
    count_surrounding_tiles()
    # display blank board
    draw_board()


def draw_board():
    print("Beginning draw_board")

    def get_x_draw(my_tile):
        return my_tile.col * globals.size_scale

    def get_y_draw(my_tile):
        return my_tile.row * globals.size_scale

    def get_image(my_tile):
        # if bomb
        if my_tile.is_bomb:
            return "bomb"

        # if empty
        if my_tile.bomb_count == 0:
            return "empty"

        # otherwise, get count
        return my_tile.bomb_count

    for row in globals.list_of_tiles:
        for current_tile in row:
            # get the pygame image to display
            image_type = get_image(current_tile)
            image_name = f"assets/{image_type}.png"
            py_image = pygame.image.load(image_name)
            py_image = pygame.transform.scale(py_image, (globals.size_scale, globals.size_scale))

            # get the coordinates of top left corner to draw tile image
            draw_coordinates = get_x_draw(current_tile), get_y_draw(current_tile)
            globals.screen.blit(py_image, draw_coordinates)
            print(current_tile)

    print("Finish draw_board")


if __name__ == '__main__':
    # configure assets
    list_of_assets = os.listdir(os.getcwd() + "/assets")
    for i in list_of_assets:
        print(i)

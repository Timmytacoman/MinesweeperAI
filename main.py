import math

import pygame
import argparse
import random
import sys
import math

sys.setrecursionlimit(1000000)

# default board edge size
default_edge_size = 20

# bomb percentage
bomb_percentage = 1
num_bombs = 0

# instantiate the parser
parser = argparse.ArgumentParser(description='Specify game parameters')

# add arguments for rows and cols
parser.add_argument('--size', type=int, default=default_edge_size, help="enter the size of the board to generate")

# collect input size
args = parser.parse_args()
size = args.size

# screen dimensions
screen_size = size * 40

print(f"Generating board size: {size}")
print(f"Screen size: {screen_size}")

# init the pygame library
pygame.init()

# set the pygame window name
pygame.display.set_caption('Minesweeper AI')

# determine tile length
tile_length = screen_size / size
print(f"tileLength = {tile_length}")

# Set up the drawing window
screen = pygame.display.set_mode([screen_size, screen_size])

# global list of all the tile objects
list_of_tiles = []

list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8]


def getScaledImage(name):
    # returns the scaled image of the desired image
    return pygame.transform.scale(pygame.image.load(f"./assets/{name}.png"), (tile_length, tile_length))


# image constructing
tile_image = getScaledImage('tile')
empty_image = getScaledImage('empty')
bomb_image = getScaledImage('bomb')
flag_image = getScaledImage('flag')
one_image = getScaledImage('1')
two_image = getScaledImage('2')
three_image = getScaledImage('3')
four_image = getScaledImage('4')
five_image = getScaledImage('5')
six_image = getScaledImage('6')
seven_image = getScaledImage('7')
eight_image = getScaledImage('8')


class Tile:
    def __init__(self, x, y, is_bomb, image=None):
        # x and y denote the top left position of the tile
        self.x = x
        self.y = y
        self.is_bomb = is_bomb
        self.image = image
        self.bomb_count = None
        self.is_visited = False

    def __str__(self):
        # this is called when you print a Tile object
        return str(f"x={self.x}\ny={self.y}\nis_bomb={self.is_bomb}\nbomb_count={self.bomb_count}")

    def set_image(self, image=None):
        if image is not None:
            self.image = image
            return
        convert_to_word = {
            None: bomb_image,
            0: empty_image,
            1: one_image,
            2: two_image,
            3: three_image,
            4: four_image,
            5: five_image,
            6: six_image,
            7: seven_image,
            8: eight_image
        }
        self.image = convert_to_word[self.bomb_count]

    def set_bomb_count(self, count):
        self.bomb_count = count

    def set_visited(self, status):
        self.is_visited = status


def init_board():
    # initialize the board

    # construct all the tiles
    for row in range(size):
        for col in range(size):
            # construct tile obj
            x = col * tile_length
            y = row * tile_length

            # randomize bombs
            is_bomb = False
            rand_num = random.randint(1, 100)
            if 1 <= rand_num <= bomb_percentage:
                is_bomb = True
                global num_bombs
                num_bombs += 1
            # create tile
            new_tile = Tile(x, y, is_bomb, tile_image)
            # append it to list
            list_of_tiles.append(new_tile)
            # draw tiles
            # screen.blit(tile_image, (x, y))

    pygame.display.flip()


def process_board():
    # for every tile we need to pre-process the surrounding tiles

    for tile in list_of_tiles:
        # if it's already a bomb, we don't care about surrounding values
        if tile.is_bomb:
            continue
        surrounding_bomb_count = 0
        for row in range(-1, 2):
            for col in range(-1, 2):
                # skip checking current spot
                if row == 0 and col == 0:
                    continue
                # collect search coordinates
                x_search = tile.x + (col * tile_length)
                y_search = tile.y + (row * tile_length)
                # find adj tile
                for t in list_of_tiles:
                    if (t.x == x_search) and (t.y == y_search):
                        if t.is_bomb:
                            surrounding_bomb_count += 1
                        break

        tile.set_bomb_count(surrounding_bomb_count)
        # print(surrounding_bomb_count)


def draw_board():
    for tile in list_of_tiles:
        screen.blit(tile.image, (tile.x, tile.y))
    pygame.display.flip()


def on_left_click(x, y):
    clicked_tile = None
    shortest = tile_length

    # determine what tile was closest
    for tile in list_of_tiles:
        # distance formula
        x_distance = abs(tile.x + (tile_length / 2) - x)
        y_distance = abs(tile.y + (tile_length / 2) - y)
        distance = x_distance + y_distance
        if distance < shortest:
            shortest = distance
            clicked_tile = tile

    clicked_tile.set_image()

    # if the clicked tile was a bomb
    if clicked_tile.is_bomb:
        on_death()
        return clicked_tile

    # if not a bomb, set respective image
    if clicked_tile.bomb_count in list_of_nums:
        return

    # find surrounding
    if clicked_tile.bomb_count == 0:
        search_surrounding_tiles(clicked_tile)
        return


def on_right_click(x, y):
    clicked_tile = None
    shortest = tile_length

    # determine what tile was closest
    for tile in list_of_tiles:
        # distance formula
        x_distance = abs(tile.x + (tile_length / 2) - x)
        y_distance = abs(tile.y + (tile_length / 2) - y)
        distance = x_distance + y_distance
        if distance < shortest:
            shortest = distance
            clicked_tile = tile

    # toggle flags
    if clicked_tile.image == tile_image or clicked_tile.image == flag_image:
        if clicked_tile.image == flag_image:
            clicked_tile.set_image(tile_image)
        else:
            clicked_tile.set_image(flag_image)


remaining_tiles_to_search = []

count = 0


def search_surrounding_tiles(tile):
    global count
    print(f"Iteration = {count}")
    print("Searching from:")
    print(f"---- \n{tile}\n-----")

    tile.is_visited = True

    for row in range(-1, 2):
        for col in range(-1, 2):
            # skip checking current spot
            if row == 0 and col == 0:
                continue
            # collect search coordinates
            x_search = tile.x + (col * tile_length)
            y_search = tile.y + (row * tile_length)
            # find adj tile
            for t in list_of_tiles:
                if (t.x == x_search) and (t.y == y_search):
                    # found adj tile

                    # if its already been visited, continue
                    if t.is_visited:
                        continue

                    # if empty tile
                    if t.bomb_count == 0:
                        # add tile to list
                        remaining_tiles_to_search.append(t)
                        # set tile image to empty
                        t.set_image()

                        # recurse
                        search_surrounding_tiles(t)

                    # otherwise, display num
                    else:
                        if t.bomb_count is not None:
                            t.set_image()
                            print(t)
                            break

    print(remaining_tiles_to_search)

    count += 1


def on_death():
    print("you died")
    screen.fill((255, 0, 0))
    global running
    running = False


def check_win():
    print("checking win")
    global running
    num_cleared_tiles = 0
    for tile in list_of_tiles:
        if tile.image is not bomb_image and tile.image is not tile_image and tile.image is not flag_image:
            num_cleared_tiles += 1
    print(size * size - num_bombs, num_cleared_tiles)
    if size * size - num_bombs == num_cleared_tiles:
        # WIN!
        print("Winner!")
        screen.fill((0, 255, 0))
        running = False


# initialize the board
init_board()

# process the board
process_board()

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

            click_type = event.button

            print(click_type)

            x_click, y_click = pygame.mouse.get_pos()

            # left click
            if click_type == 1:
                print('1')
                # declare position
                print(on_left_click(x_click, y_click))
                check_win()

            # right click
            if click_type == 3:
                print('3')
                # declare position
                print(on_right_click(x_click, y_click))

# Done! Time to quit.
pygame.display.flip()
pygame.time.delay(2000)
print("Goodbye!")
pygame.quit()

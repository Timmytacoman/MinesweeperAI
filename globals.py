import numpy as np
import tile
import pygame

# start global variable declarations -----------------

# screen obj for pygame
screen = None

# bomb percentage
bomb_percentage = 15

# size of board to generate (size n default)
size = 10
size_scale = 40

# list of tile obj
list_of_tiles = None


def create_tiles(x):
    global list_of_tiles
    list_of_tiles = np.ndarray((x, x), tile.Tile)


# add start time
start_time = None

# add images here for enhanced rendering
# index order:
# 0     :    tile.png
# 1-8   :     1-8.png
# 9     :    bomb.png
# 10    :   empty.png
# 11    :    flag.png

display_images = []

# add 1-8
for i in range(1, 9):
    image_name = f"assets/{i}.png"
    py_image = pygame.image.load(image_name)
    py_image = pygame.transform.scale(py_image, (size_scale, size_scale))
    display_images.append(py_image)

for i in ["tile", "bomb", "empty", "flag"]:
    image_name = f"assets/{i}.png"
    py_image = pygame.image.load(image_name)
    py_image = pygame.transform.scale(py_image, (size_scale, size_scale))
    if i == "tile":
        display_images.insert(0, py_image)
    elif i == "bomb":
        display_images.insert(9, py_image)
    elif i == "empty":
        display_images.insert(10, py_image)
    elif i == "flag":
        display_images.insert(11, py_image)

# end global variable declarations -----------------

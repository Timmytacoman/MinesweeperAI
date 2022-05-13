import numpy as np
import tile

# start global variable declarations -----------------

# screen obj for pygame
screen = None

# bomb percentage
bomb_percentage = 30

# size of board to generate (size n default)
size = 10
size_scale = 40

# list of tile obj
list_of_tiles = None


def create_tiles(x):
    global list_of_tiles
    list_of_tiles = np.ndarray((x, x), tile.Tile)

# end global variable declarations -----------------

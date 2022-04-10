import driver
import random
import globals


class Tile:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.is_bomb = False
        self.bomb_count = 0

    def __str__(self):
        return f"row = {self.row} \n" \
               f"col = {self.col} \n" \
               f"is_bomb = {self.is_bomb} \n" \
               f"bomb_count = {self.bomb_count}"

    def set_bomb(self):
        self.is_bomb = True

    def set_bomb_count(self, num):
        self.bomb_count = num


def construct_tiles():
    print("Beginning tile construction")

    def randomize_bomb(current_tile):
        # randomize the bomb creation
        rand_num = random.randint(1, 100)
        if 1 <= rand_num <= globals.bomb_percentage:
            current_tile.set_bomb()

    for row in range(globals.size):
        for col in range(globals.size):
            # create new tile
            new_tile = Tile(row, col)
            randomize_bomb(new_tile)
            globals.list_of_tiles[row][col] = new_tile

    print("Finished tile construction")

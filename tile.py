import driver
import random


class Tile:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.is_bomb = False

    def __str__(self):
        return f"row = {self.row} \n" \
               f"col = {self.col} \n" \
               f"is_bomb = {self.is_bomb}"

    def set_bomb(self):
        self.is_bomb = True


def construct_tiles():
    print("Beginning tile construction")

    def randomize_bomb(current_tile):
        # randomize the bomb creation
        rand_num = random.randint(1, 100)
        if 1 <= rand_num <= driver.bomb_percentage:
            current_tile.set_bomb()

    for row in range(driver.size):
        for col in range(driver.size):
            # create new tile
            new_tile = Tile(row, col)
            randomize_bomb(new_tile)
            driver.list_of_tiles[row][col] = new_tile

    print("Finished tile construction")

import os
import driver
import tile


def count_surrounding_tiles():
    print("Beginning counting surrounding tiles")

    print("Finishing counting surrounding tiles")


def setup_board():
    # construct all tiles with chance of bomb
    tile.construct_tiles()
    # determine surrounding bomb counts
    count_surrounding_tiles()


def draw_board():
    pass


if __name__ == '__main__':
    # configure assets
    list_of_assets = os.listdir(os.getcwd() + "/assets")
    for i in list_of_assets:
        print(i)

import pprint 

from day9_1 import Tile


def input_to_tiles(input_str: str) -> list[Tile]:
    input_coordinates = [c for c in input_str.split("\n") if c != '']

    coordinates = []
    for line in input_coordinates:
        x, y = line.split(",")
        coordinates.append(Tile(x=int(x), y=int(y)))
    return coordinates


def tiles_to_grid(tiles: list[Tile]) -> list[list[str]]:
    max_x = max(t.x for t in tiles)
    max_y = max(t.y for t in tiles)
    
    # Shape grid that encompasses all tiles with a margin of 1 
    margin = 1
    grid = [
        ['.'] * (max_x+1+margin)
    ] * (max_y+1+margin)

    grid[0][1] = '#'
    assert False, grid[1]


    return grid


def get_green_tile_coordinates(grid: list[list[str]], tile_coordinates: tuple[int, int]):
    green_tiles = []

    for tile in tile_coordinates:
        x = tile.x
        # Walk grid along X axis
        ## left
        while x > 0:
            x -= 1
            character = grid[tile.y][x]
            if character == '#':
                for x_i in range(x, tile.x):
                    green_tiles.append(
                        (x_i, tile.y)
                    )
                break

        ## right
        while x < len(grid[0])-1:
            x += 1
            character = grid[tile.y][x]
            if character == '#':
                for x_i in range(tile.x, x):
                    green_tiles.append(
                        (x_i, tile.y)
                    )
                break

        # Walk grid along Y axis
        y = tile.y
        ## up
        while y > 0:
            y -= 1
            character = grid[y][tile.x]
            if character == '#':
                for y_i in range(y, tile.y):
                    green_tiles.append(
                        (tile.x, y_i)
                    )
                break

        ## right
        while y < len(grid)-1:
            y += 1
            character = grid[y][tile.x]
            if character == '#':
                for y_i in range(tile.y, y):
                    green_tiles.append(
                        (tile.x, y_i)
                    )
                break

    return green_tiles



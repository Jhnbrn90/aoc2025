from day4_part1 import get_adjacent_coordinates


def get_removable_roll_coordinates(grid: list[list[str]]) -> list[tuple[int, int]]:
    removable_roll_coordinates = []

    for y, row in enumerate(grid):
        for x, column in enumerate(row):
            if column == '.' or column == 'x':
                continue

            adjacent_count = 0
            adjacent_coordinates = get_adjacent_coordinates(x, y)

            for x_i, y_i in adjacent_coordinates:
                if x_i <= len(row)-1 and y_i <= len(grid)-1:
                    if grid[y_i][x_i] == '@':
                        adjacent_count += 1

            if adjacent_count < 4:
                removable_roll_coordinates.append((x, y))

    return removable_roll_coordinates


def remove_adjacent_rolls(grid: list[list[str]]):
    total_removed_rolls = 0
    removable_roll_coordinates = get_removable_roll_coordinates(grid)

    while removable_roll_coordinates != []:
        removable_roll_coordinates = get_removable_roll_coordinates(grid)
        removed_rolls = len(removable_roll_coordinates)
        total_removed_rolls += removed_rolls

        for x_i, y_i in removable_roll_coordinates:
            grid[y_i][x_i] = 'x'

    return total_removed_rolls

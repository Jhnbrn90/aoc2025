def parse_grid(grid_str: str) -> list[list[str]]:
    grid = []

    for row in grid_str.strip().split('\n'):
        grid.append([c for c in row])

    return grid


def get_adjacent_coordinates(x: int, y: int):
    """Get the neighbouring coordinates for a given position."""
    # Keep track of adjacent fields
    adjacent_fields = []

    # All possible adjacent positions: (x, y)
    adjacent_coordinates = [
        (0, 1),  # up
        (0, -1),  # down
        (-1, 0),  # left
        (1, 0),  # right
        (-1, 1),  # left up
        (-1, -1),  # left down
        (1, 1),  # right up
        (1, -1),  # right down
    ]

    for x_i, y_i in adjacent_coordinates:
        new_x = x + x_i
        new_y = y + y_i

        if new_x >= 0 and new_y >= 0:
            adjacent_fields.append((new_x, new_y))

    return adjacent_fields


def walk_grid_adjacent_rolls(grid: list[list[str]]) -> int:
    accessible_rolls = 0

    for y, row in enumerate(grid):
        for x, column in enumerate(row):
            if column == '.':
                continue

            adjacent_count = 0
            adjacent_coordinates = get_adjacent_coordinates(x, y)

            for x_i, y_i in adjacent_coordinates:
                if x_i <= len(row)-1 and y_i <= len(grid)-1:
                    if grid[y_i][x_i] == '@':
                        adjacent_count += 1

            if adjacent_count < 4:
                accessible_rolls += 1

    return accessible_rolls

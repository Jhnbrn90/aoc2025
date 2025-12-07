import pprint

def walk_up_grid(grid: list[list[str]]):
    routes = []
    for x, character in enumerate(grid[0]):
        if character == '|':
            # Follow path(s) for this route to start
            routes.append(follow_path(grid, x=x, y=0))

    return routes


def follow_path(grid, x, y):
    """Return new coordinates to continue path."""
    if y >= len(grid)-1:
        return 1

    # Move up the grid:
    match grid[y+1][x]:
        case '|' | 'S':
            # Simply follow the beam
            return follow_path(grid, x, y+1)
        case '.':
            # Two possibilities:
            # - splitter on left side (y+1, x-1); OR
            # - splitter on the right side (y+1, x+1)
            if x-1 >= 0 and x < len(grid[y+1])-1:
                if grid[y+1][x-1] == '^' and grid[y+1][x+1] == '^':
                    return follow_path(grid, x-1, y+1) + follow_path(grid, x-1, y+1)
            if x-1 >= 0:
                if grid[y+1][x-1] == '^':
                    return follow_path(grid, x-1, y+1)

            if x+1 < len(grid[y+1])-1:
                if grid[y+1][x+1] == '^':
                        return follow_path(grid, x+1, y+1)

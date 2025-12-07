from functools import cache

@cache
def walk_grid(grid: list[list[str]], x, y):
    if y >= len(grid):
        # Fully walked route until the end
        return 1

    match grid[y][x]:
        case '.' | 'S':
            return walk_grid(grid, x, y+1)
        case '^':
            return walk_grid(grid, x-1, y) + walk_grid(grid, x+1, y)


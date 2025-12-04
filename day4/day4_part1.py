def parse_grid(grid_str: str) -> list[list[str]]:
    grid = []

    for row in grid_str.strip().split('\n'):
        grid.append([c for c in row])

    return grid

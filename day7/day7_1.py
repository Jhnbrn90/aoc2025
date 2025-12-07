def step_down_grid(grid: list[list[str]], y: int = 0, split_count: int = 0):
    # Check if we've reached the end
    last_row = len(grid)-1
    if y == last_row:
        # we can't split the beam anymore
        return grid, split_count

    # Look at the columns of the current row
    for x, character in enumerate(grid[y]):
        match character:
            case '.':
                pass
            case 'S':
                # Start the beam directly below
                grid[y+1][x] = '|'
            case '^':
                # Check if we have beam to split above (y-1)
                if grid[y-1][x] == '|':
                    split_count += 1
                    # Draw new beams below, on (y+1, x-1) and (y+1, x+1)
                    grid[y+1][x-1] = '|'
                    grid[y+1][x+1] = '|'
            case '|':
                # Check what is below the beam
                if grid[y+1][x] == '.':
                    # Prolongate beam
                    grid[y+1][x] = '|'
                
                # If there is a splitter below the beam, it will be handled
                # in the `case '^'` splitter case
            case _:
                raise ValueError(f"Other character encountered: {character}.")

    return step_down_grid(grid, y+1, split_count)

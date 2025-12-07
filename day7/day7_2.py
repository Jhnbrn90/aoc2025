def step_down_grid(grid: list[list[str]], y: int = 0, touched_splitters = None):
    """This time we're interested in which splitters are touched.

    The total amount of options is calculated by 2^n, where `n` is the amount
    of touched splitters.
    """
    touched_splitters = [] if touched_splitters is None else touched_splitters

    # Check if we've reached the end
    last_row = len(grid)-1
    if y == last_row:
        # we can't split the beam anymore
        return touched_splitters

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
                    touched_splitters.append((x, y))
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

    return step_down_grid(grid, y+1, touched_splitters)

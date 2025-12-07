def step_down_grid(grid: list[list[str]], y: int = 0, overlaps: int = 0, split_count: int = 0):
    """This time we're interested in which splitters are touched.

    The total amount of options is calculated by 2^n, where `n` is the amount
    of touched splitters.
    """
    # Check if we've reached the end
    last_row = len(grid)-1
    if y == last_row:
        # we can't split the beam anymore
        return grid, overlaps, split_count

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
                    for x_split in (x-1, x+1):
                        if grid[y+1][x_split] == '|':
                            # If there is a beam already, we're double counting
                            overlaps += 1 
                        else:
                            grid[y+1][x_split] = '|'
            case '|':
                # Check what is below the beam
                if grid[y+1][x] == '.':
                    # Prolongate beam
                    grid[y+1][x] = '|'
                
                # If there is a splitter below the beam, it will be handled
                # in the `case '^'` splitter case
            case _:
                raise ValueError(f"Other character encountered: {character}.")

    return step_down_grid(grid, y+1, overlaps, split_count)

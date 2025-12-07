import pprint

from day7_1 import step_down_grid
from day7_2 import walk_up_grid


def main():
    with open('day7/sample_input.txt') as f:
        puzzle_input = f.read()
    
    # Day 2
    grid = [list(c) for c in puzzle_input.split('\n') if c != '']
    traversed_grid, split_count = step_down_grid(grid)

    reversed_grid = traversed_grid[::-1]

    # Day 2
    routes = walk_up_grid(reversed_grid)
    assert False, sum(routes)

    print(f"Timelines: {timelines}")


if __name__ == "__main__":
    main()

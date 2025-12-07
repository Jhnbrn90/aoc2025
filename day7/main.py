import pprint

from day7_2 import step_down_grid


def main():
    with open('day7/puzzle_input.txt') as f:
        puzzle_input = f.read()
    
    # Day 2
    grid = [list(c) for c in puzzle_input.split('\n') if c != '']
    grid, overlaps, split_count = step_down_grid(grid)

    routes = grid[-1].count('|')

    timelines = routes+overlaps+split_count

    print(f"Timelines: {timelines}")


if __name__ == "__main__":
    main()

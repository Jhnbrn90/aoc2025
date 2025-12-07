import pprint

from day7_1 import step_down_grid


def main():
    with open('day7/sample_input.txt') as f:
        puzzle_input = f.read()
    
    # To grid
    grid = [list(c) for c in puzzle_input.split('\n') if c != '']

    grid, split_count = step_down_grid(grid)

    pprint.pp(grid)

    print(f"Split number of times: {split_count}")


if __name__ == "__main__":
    main()

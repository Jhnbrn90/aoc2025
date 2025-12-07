import pprint

from day7_2 import step_down_grid


def main():
    with open('day7/sample_input.txt') as f:
        puzzle_input = f.read()
    
    # Day 2
    grid = [list(c) for c in puzzle_input.split('\n') if c != '']
    touched_splitters = set(step_down_grid(grid))

    amount_of_timelines = pow(2, len(touched_splitters))
    print(f"Amount of possible timelines: {amount_of_timelines}")


if __name__ == "__main__":
    main()

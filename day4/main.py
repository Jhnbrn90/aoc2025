from day4_part1 import (
    parse_grid,
    walk_grid_adjacent_rolls,
)


def main():
    with open('day4/puzzle_input.txt') as f:
        puzzle_input = f.read()

    grid = parse_grid(puzzle_input)

    number_of_accessible_rolls = walk_grid_adjacent_rolls(grid)

    print(f"Accessible rolls: {number_of_accessible_rolls}")

if __name__ == "__main__":
    main()

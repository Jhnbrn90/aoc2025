from day4_part1 import parse_grid


def main():
    with open('day4/sample_input.txt') as f:
        puzzle_input = f.read()

    print(parse_grid(puzzle_input))


if __name__ == "__main__":
    main()

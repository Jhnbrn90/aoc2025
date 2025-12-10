from day10_1 import (
    Machine,
    parse_input_str_to_parts,
    find_shortest_path,
)


def main():
    with open('day_10/puzzle_input.txt') as f:
        puzzle_input = f.read().strip()

    total_min_path = 0
    for i, machine_input in enumerate(puzzle_input.split("\n")):
        machine_str, buttons = parse_input_str_to_parts(machine_input)

        machine = Machine(machine_str)
        found_path = find_shortest_path(machine, buttons)
        total_min_path += found_path
        print(f"Found shortest path for line {i+1}: {found_path}")

    print(f"Day 1: least amount of buttons: {total_min_path}")


if __name__ == "__main__":
    main()

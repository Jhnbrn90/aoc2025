from day10_1 import (
    Machine,
    parse_input_str_to_parts,
    find_shortest_path,
)

from day10_2 import (
    parse_machine,
    find_possible_button_combinations,
    possible_patterns,
    minimum_presses_reaching_state,
    minimum_presses_reaching_joltages,
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

    print(f"Day 1: least amount of buttons: {total_min_path}")

    # Day 2
    button_presses = 0

    for line in puzzle_input.split("\n"):
        indicators, buttons, joltages = parse_machine(line)

        patterns = possible_patterns(buttons)
        minimum_presses = minimum_presses_reaching_joltages(joltages, patterns)

        button_presses += minimum_presses

    print(f"Day 2: least amount of buttons: {button_presses}")


if __name__ == "__main__":
    main()

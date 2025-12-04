from day3_part1 import (
    max_joltage_from_battery_bank,
    parse_battery_string_to_bank_list,
)


from day3_part2 import (
    select_batteries_from,
    list_batteries_to_joltage,
)


def main():
    with open('day3/puzzle_input.txt') as f:
        puzzle_input = f.read()

    # Day 1
    total_joltage = 0
    for battery_bank_string in puzzle_input.strip().split('\n'):
        battery_bank_list = parse_battery_string_to_bank_list(battery_bank_string)
        total_joltage += max_joltage_from_battery_bank(battery_bank_list)

    print(f"The total joltage: {total_joltage}")

    # Day 2
    select_amount = 12
    total_joltage = 0

    for battery_bank_string in puzzle_input.strip().split('\n'):
        battery_bank_list = parse_battery_string_to_bank_list(battery_bank_string)
        selected_batteries = select_batteries_from(battery_bank_list, select_amount)
        total_joltage += list_batteries_to_joltage(selected_batteries)

    print(f"The total joltage: {total_joltage}")


if __name__ == "__main__":
    main()

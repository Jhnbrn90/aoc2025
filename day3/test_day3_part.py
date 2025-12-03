import pytest

from day3_part1 import (
    max_joltage_from_battery_bank,
    parse_battery_string_to_bank_list,
)



@pytest.mark.parametrize('battery_string, expected_list', [
    ('98765432111', [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1]),
])
def test_parse_battery_string(battery_string: str, expected_list: list[int]):
    assert parse_battery_string_to_bank_list(battery_string) == expected_list


@pytest.mark.parametrize('battery_bank,expected_joltage', [
    ('987654321111111', 98),
    ('811111111111119', 89),
    ('234234234234278', 78),
    ('818181911112111', 92),
])
def test_max_joltage_from_battery_bank(battery_bank: str, expected_joltage: int):
    battery_bank_list = parse_battery_string_to_bank_list(battery_bank)

    result = max_joltage_from_battery_bank(battery_bank_list)
    assert result == expected_joltage


def test_sample_input():
    with open('day3/sample_input.txt') as f:
        puzzle_input = f.read()

    total = 0
    for battery_bank_string in puzzle_input.strip().split('\n'):
        battery_bank_list = parse_battery_string_to_bank_list(battery_bank_string)
        total += max_joltage_from_battery_bank(battery_bank_list)

    assert total == 357


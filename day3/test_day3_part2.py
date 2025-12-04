import pytest

from day3_part1 import parse_battery_string_to_bank_list

from day3_part2 import (
    list_batteries_to_joltage,
    get_index_for_highest_joltage,
    get_selection_window,
    select_index_using_window,
    select_batteries_from,
)


@pytest.mark.parametrize('battery_bank,expected_index', [
    ([9, 9, 9, 8], 0),
    ([8, 9, 1, 2], 1),
    ([8, 8, 9, 9, 8], 2),
    ([0, 0, 1, 0, 0, 1], 2),
])
def test_highest_battery_joltage_index(battery_bank: list[int], expected_index: int):
    assert get_index_for_highest_joltage(battery_bank) == expected_index


@pytest.mark.parametrize('battery_bank,amount_to_select,expected_window', [
    ([2, 1, 3, 4, 0], 1, [2, 1, 3, 4, 0]),  # all batteries when we only select 1
    ([2, 1, 3, 4, 0], 2, [2, 1, 3, 4]),  # should exclude the "0" to total 2 batteries
    ([2, 1, 3, 4, 0], 3, [2, 1, 3]),  # should exclude the "0", "4" to total 3 batteries
    ([2, 1, 3, 4, 0], 4, [2, 1]),  # leave out "3", "4" and "0" to make up 4 battieries
    ([2, 1, 3, 4, 0], 5, [2]),  # we must take the first value, as we'll select all batteries
])
def test_selection_window(battery_bank: list[int], amount_to_select: int, expected_window: list[int]):
    assert get_selection_window(battery_bank, amount_to_select) == expected_window


@pytest.mark.parametrize('battery_bank,amount_to_select,expected_index',[
    ([1, 2, 7, 6, 4], 1, 2),  # should select highest
    ([1, 2, 7, 6, 4], 2, 2),  # highest from "1", 2", "7", "6" 
    ([1, 2, 7, 6, 4], 3, 2),  # highest from "1", "2", "7"
    ([1, 2, 7, 6, 4], 4, 1),  # should select "2" from "1"/"2" since we need 3 more
    ([1, 2, 7, 6, 4], 5, 0),  # should select "1" as we need all
])
def test_select_index_windowed(battery_bank: list[int], amount_to_select:int, expected_index: int):
    """Check that we can select the left-most highest battery given selection."""
    assert select_index_using_window(battery_bank, amount_to_select) == expected_index


@pytest.mark.parametrize('battery_bank,amount_to_select, expected_selection', [
    ([1, 2, 7, 6, 4], 2, [7, 6]),
])
def test_get_maximum_joltage_from_battery_bank(battery_bank: list[int], amount_to_select: int, expected_selection: list[int]):
    result = select_batteries_from(battery_bank, amount_to_select)
    assert result == expected_selection


@pytest.mark.parametrize('battery_list,expected_joltage', [
    ([1, 2, 3], 123),
    ([9, 9, 8, 7, 6, 5, 4, 3], 99876543),
])
def test_convert_list_of_batteries_to_joltage(battery_list: list[int], expected_joltage: int):
    assert list_batteries_to_joltage(battery_list) == expected_joltage


@pytest.mark.parametrize('battery_bank,expected_joltage', [
    ('987654321111111', 987654321111),
])
def test_string_battery_bank_from_example(battery_bank: str, expected_joltage: int):
    select_amount_of_batteries = 12
    battery_bank_list = parse_battery_string_to_bank_list(battery_bank)

    selected_batteries = select_batteries_from(battery_bank_list, select_amount_of_batteries)

    result = list_batteries_to_joltage(selected_batteries)

    assert result == expected_joltage


def test_example_input():
    with open('day3/sample_input.txt') as f:
        puzzle_input = f.read()

    select_amount = 12
    total_joltage = 0

    for battery_bank_string in puzzle_input.strip().split('\n'):
        battery_bank_list = parse_battery_string_to_bank_list(battery_bank_string)
        selected_batteries = select_batteries_from(battery_bank_list, select_amount)
        total_joltage += list_batteries_to_joltage(selected_batteries)

    assert total_joltage == 3121910778619

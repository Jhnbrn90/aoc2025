import pytest

from part_1 import (
    range_list_to_dict,
    get_fresh_ingredients_from_ranges,
    parse_input,
)


@pytest.mark.parametrize('range_str_list,expected_dict', [
    (['3-5', '16-20'], {3: [range(3, 6)], 16: [range(16, 21)]}),
    (['3-5', '3-19'], {3: [range(3, 6), range(3, 20)]}),
])
def test_range_dict_from_list_of_strings(range_str_list: list[str], expected_dict: dict[int, range]):
    """Check input ranges are converted to inclusive `range`."""
    assert range_list_to_dict(range_str_list) == expected_dict


@pytest.mark.parametrize('ranges,available_ingredients,expected_fresh_ingredients', [
    ({1: [range(1, 3), range(1, 2), range(1, 8)], 14: [range(14, 19)]}, [1, 31, 2, 4, 5, 7, 18, 19, 21, 20], {1, 2, 4, 5, 7, 18}),
    ({3: [range(3, 6)], 10: [range(10, 15)], 16: [range(16, 21)], 12: [range(12, 19)]}, [1, 5, 8, 11, 17, 32], {5, 11, 17}),
])
def test_select_fresh_ingredients(ranges: list[range], available_ingredients: list[int], expected_fresh_ingredients: list[int]):
    """Check if the fresh ingredients can be obtained from the ranges."""

    fresh_ingredients = get_fresh_ingredients_from_ranges(
        ranges,
        available_ingredients,
    )

    assert fresh_ingredients == expected_fresh_ingredients


def test_parse_puzzle_input():
    with open('day5/sample_input.txt') as f:
        puzzle_input = f.read()

    ranges, available_ingredients = parse_input(puzzle_input)

    assert ranges == {
        3: [range(3, 6)],
        10: [range(10, 15)],
        16: [range(16, 21)],
        12: [range(12, 19)],
    }

    assert available_ingredients == [
        1,
        5,
        8,
        11,
        17,
        32
    ]


def test_sample_puzzle_input():
    with open('day5/sample_input.txt') as f:
        puzzle_input = f.read()

    ranges, available_ingredients = parse_input(puzzle_input)

    fresh_ingredients = get_fresh_ingredients_from_ranges(
        ranges,
        available_ingredients,
    )

    assert fresh_ingredients == {5, 11, 17}

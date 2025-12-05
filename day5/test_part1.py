import pytest

from part_1 import (
    combine_ranges,
    get_fresh_ingredients_from_ranges,
    parse_input,
    str_to_range,
)


@pytest.mark.parametrize('range_str,expected_range', [
    ('3-5', range(3, 6)),
    ('16-20', range(16, 21)),
])
def test_range_from_string(range_str: str, expected_range: range):
    """Check input ranges are converted to inclusive `range`."""
    assert str_to_range(range_str) == expected_range


@pytest.mark.parametrize('ranges,expected_ingredients', [
    ([range(1, 3), range(1, 2), range(1, 8), range(14, 19)], [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        14,
        15,
        16,
        17,
        18,
    ])
])
def test_get_full_fresh_range(ranges: list[range], expected_ingredients: list[int]):
    """Check it can get the complete range of fresh ingredients."""
    assert combine_ranges(ranges) == expected_ingredients



@pytest.mark.parametrize('ranges,available_ingredients,expected_fresh_ingredients', [
    ([range(1, 3), range(1, 2), range(1, 8), range(14, 19)], [1, 31, 2, 4, 5, 7, 18, 19, 21, 20], [1, 2, 4, 5, 7, 18]),
    ([range(3, 6), range(10, 15), range(16, 21), range(12, 19)], [1, 5, 8, 11, 17, 32], [5, 11, 17]),
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

    assert ranges == [
        range(3, 6),
        range(10, 15),
        range(16, 21),
        range(12, 19),
    ]

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

    assert fresh_ingredients == [5, 11, 17]

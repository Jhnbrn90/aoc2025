import pytest

import textwrap

from day4_part1 import (
    get_adjacent_coordinates,
    parse_grid,
    walk_grid_adjacent_rolls,
)


def test_parse_grid_from_string():
    input_grid = textwrap.dedent("""
    ..@@.@@@@.
    @@@.@.@.@@
    @@@@@.@.@@
    @.@@@@..@.
    @@.@@@@.@@
    .@@@@@@@.@
    .@.@.@.@@@
    @.@@@.@@@@
    .@@@@@@@@.
    @.@.@@@.@.
    """)

    expected_grid = [
        ['.', '.', '@', '@', '.', '@', '@', '@', '@', '.'],
        ['@', '@', '@', '.', '@', '.', '@', '.', '@', '@'],
        ['@', '@', '@', '@', '@', '.', '@', '.', '@', '@'],
        ['@', '.', '@', '@', '@', '@', '.', '.', '@', '.'],
        ['@', '@', '.', '@', '@', '@', '@', '.', '@', '@'],
        ['.', '@', '@', '@', '@', '@', '@', '@', '.', '@'],
        ['.', '@', '.', '@', '.', '@', '.', '@', '@', '@'],
        ['@', '.', '@', '@', '@', '.', '@', '@', '@', '@'],
        ['.', '@', '@', '@', '@', '@', '@', '@', '@', '.'],
        ['@', '.', '@', '.', '@', '@', '@', '.', '@', '.'],
    ]

    result = parse_grid(input_grid)

    assert result == expected_grid


def test_calculate_adjacent_rolls():
    grid = [
        ['.', '.', '@', '@', '.', '@', '@', '@', '@', '.'],
        ['@', '@', '@', '.', '@', '.', '@', '.', '@', '@'],
        ['@', '@', '@', '@', '@', '.', '@', '.', '@', '@'],
        ['@', '.', '@', '@', '@', '@', '.', '.', '@', '.'],
        ['@', '@', '.', '@', '@', '@', '@', '.', '@', '@'],
        ['.', '@', '@', '@', '@', '@', '@', '@', '.', '@'],
        ['.', '@', '.', '@', '.', '@', '.', '@', '@', '@'],
        ['@', '.', '@', '@', '@', '.', '@', '@', '@', '@'],
        ['.', '@', '@', '@', '@', '@', '@', '@', '@', '.'],
        ['@', '.', '@', '.', '@', '@', '@', '.', '@', '.'],
    ]

    assert walk_grid_adjacent_rolls(grid) == 13


@pytest.mark.parametrize('x,y,expected_adjacent_coordinates', [
    (0, 0, [(0, 1), (1, 0), (1, 1)]),  # do not include -1 values
    (5, 2, [
        (5, 3),  # up
        (5, 1),  # down
        (4, 2),  # left
        (6, 2),  # right
        (4, 3),  # left,down
        (4, 1),  # left,up
        (6, 3),  # right,down
        (6, 1),  # right,up
    ]),
])
def test_adjacent_coordinates(x: int, y: int, expected_adjacent_coordinates: int):
    assert get_adjacent_coordinates(x, y) == expected_adjacent_coordinates

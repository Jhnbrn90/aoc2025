import pytest

from day6_1 import (
    calculate_single_line,
    parse_input_string_to_grid,
    problem_to_single_line,
    transpose_math_problem_matrix,
)


@pytest.mark.parametrize('math_problem,as_string', [
    (['2', '3', '4', '*'], '2*3*4'),
    (['115', '12', '4', '+'], '115+12+4'),
])
def test_calculate_single_line(math_problem: list[str], as_string: str):
    assert problem_to_single_line(math_problem) == as_string


@pytest.mark.parametrize('math_problem,answer', [
    (['2', '3', '4', '*'], 24),
])
def test_calculate_single_line(math_problem: list[str], answer: int):
    assert calculate_single_line(math_problem) == answer


def test_parse_2d_matrix_to_math_problems():
    # Given we have a grid of math problems
    math_problems = [
        ['123', '328', '51', '64'],
        ['45', '64', '387', '23'],
        ['6', '98', '215', '314'],
        ['*', '+', '*', '+'],
    ]


    # When we transpose the matrix
    transposed_matrix = transpose_math_problem_matrix(math_problems)

    # We expect the following form:
    assert transposed_matrix == [
        ['123', '45', '6', '*'],
        ['328', '64', '98', '+'],
        ['51', '387', '215', '*'],
        ['64', '23', '314', '+'],
    ]


def test_parse_input_string_to_grid():
    math_problems = [
        ['123', '328', '51', '64'],
        ['45', '64', '387', '23'],
        ['6', '98', '215', '314'],
        ['*', '+', '*', '+'],
    ]

    with open('day6/sample_input.txt') as f:
        puzzle_input = f.read()

    assert parse_input_string_to_grid(puzzle_input) == math_problems


def test_calculate_sample_input():
    with open('day6/sample_input.txt') as f:
        puzzle_input = f.read()

    problem_grid = parse_input_string_to_grid(puzzle_input)
    math_problem_lines = transpose_math_problem_matrix(problem_grid)

    total = 0
    for math_problem_line in math_problem_lines:
        total += calculate_single_line(math_problem_line)

    assert total == 4277556

import pytest
import textwrap


from day6_1 import transpose_math_problem_matrix
from day6_2 import parse_input_string_to_grid, calculate_problem_line


def test_parse_input_matrix():
    with open('day6/sample_input.txt') as f:
        puzzle_input = f.read()

    expected_matrix = [
       [
           '  4 ',
           '431 ',
           '623+',
       ],
       [
           '175 ',
           '581 ',
           ' 32*',
       ],
       [
           '8   ',
           '248 ',
           '369+',
       ],
       [
           '356 ',
           '24  ',
           '1  *',
        ]
   ]

    matrix = parse_input_string_to_grid(puzzle_input)

    assert matrix == expected_matrix

@pytest.mark.parametrize('problem_input,expected_answer', [
    (['  4 ', '431 ', '623+'], 1058),
    (['175 ', '581 ', ' 32*'], 3253600),
    (['8  ', '248 ', '369+'], 625),
    (['356 ', '24  ', '1  *'], 8544),
])
def test_calculate_math_problem(problem_input: list[str], expected_answer: int):
    assert calculate_problem_line(problem_input) == expected_answer


def test_sample_input():
    with open('day6/sample_input.txt') as f:
        puzzle_input = f.read()

    matrix = parse_input_string_to_grid(puzzle_input)

    total_sum = 0
    for row in matrix:
        total_sum += calculate_problem_line(row)

    assert total_sum == 3263827

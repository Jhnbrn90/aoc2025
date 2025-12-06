import textwrap


from day6_1 import transpose_math_problem_matrix
from day6_2 import calculate_right_left_problem

def test_parse_right_to_left():
    # Given we have a given input
    problem_input = [
        ['64 '],
        ['23 '],
        ['314'],
        ['+  '],
    ]

    transposed = transpose_math_problem_matrix(problem_input)
    assert calculate_right_left_problem(transposed[0]) == 1058

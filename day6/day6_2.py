import re


def calculate_right_left_problem(problem_input: list[str]) -> int:
    symbol = problem_input.pop()

    list_of_integers = [''.join(col) for col in zip(*problem_input)]
    combined_math_problem = f'{symbol}'.join(list_of_integers)

    return eval(combined_math_problem)


def parse_input_string_to_grid(math_problems_input: str) -> list[list[str]]:
    """Convert single string input to matrix of math problem strings."""
    matrix = []

    for row in math_problems_input.split('\n'):
        math_problem_row = [entry for entry in list(row)[::-1] if entry != ' ']

        if math_problem_row != []:
            matrix.append(math_problem_row)

    return matrix


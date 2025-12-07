import re 

from math import prod

def calculate_problem_line(math_problem: list[str]) -> int:
    symbol = math_problem[-1][-1]

    math_operation = f'{symbol}'.join(math_problem)
    return eval(math_operation[:-1])  # do not include symbol at the end


def parse_input_string_to_grid(math_problems_input: str) -> list[list[str]]:
    """Convert single string input to matrix of math problem strings."""
    new_matrix = []

    grid = [line for line in math_problems_input.split('\n') if line != '']
    cols = list(zip(*grid))
    reversed_cols = [col for col in cols[::-1]]

    # Ensure to end the series with the expected spacer
    reversed_cols.append((' ', ' ', ' '))

    math_group = []

    for entry in reversed_cols:
        condensed_entry = ''.join(entry)

        if set(condensed_entry) == {" "}:  # only contains spaces
            # End of current math problem
            new_matrix.append(math_group)
            math_group = []
        else:
            math_group.append(condensed_entry)

    return new_matrix


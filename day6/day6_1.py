def problem_to_single_line(math_problem: list[str]) -> str:
    # First, find symbol
    symbol = math_problem.pop()

    math_problem_string = f"{symbol}".join(math_problem)

    return math_problem_string

def calculate_single_line(math_problem: list[str]) -> int:
    """Calculate answer from Cephalopod math problem as list."""
    string_representation = problem_to_single_line(math_problem)

    return eval(string_representation)


def transpose_math_problem_matrix(math_problems: list[list[str]]) -> list[list[str]]:
    """Transpose the matrix to give individual problems as rows instead of columns."""
    return list(map(list, zip(*math_problems)))


def parse_input_string_to_grid(math_problems_input: str) -> list[list[str]]:
    """Convert single string input to matrix of math problem strings."""
    matrix = []

    for row in math_problems_input.split('\n'):
        math_problem_row = [entry for entry in row.split(' ') if entry != '']
        if math_problem_row != []:
            matrix.append(math_problem_row)

    return matrix


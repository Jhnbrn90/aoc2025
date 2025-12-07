from day6_1 import (
    parse_input_string_to_grid,
    transpose_math_problem_matrix,
    calculate_single_line,
)

from day6_2 import (
    calculate_right_left_problem,
    parse_input_string_to_grid as parse_grid_2,
)



def main():
    with open('day6/sample_input.txt') as f:
        puzzle_input = f.read()

    problem_grid = parse_grid_2(puzzle_input)
    math_problem_lines = transpose_math_problem_matrix(problem_grid)

    total = 0
    for math_problem_line in math_problem_lines:
        total += calculate_right_left_problem(math_problem_line)

    print(f"Total of math problems: {total}.")


if __name__ == "__main__":
    main()

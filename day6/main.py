from day6_1 import (
    parse_input_string_to_grid,
    transpose_math_problem_matrix,
    calculate_single_line,
)

from day6_2 import (
    calculate_problem_line,
    parse_input_string_to_grid as parse_grid_2,
)



def main():
    with open('day6/puzzle_input.txt') as f:
        puzzle_input = f.read()

    # Day 2
    matrix = parse_grid_2(puzzle_input)

    total = 0
    for row in matrix:
        total += calculate_problem_line(row)

    print(f"Total of math problems: {total}")


if __name__ == "__main__":
    main()

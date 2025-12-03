# from puzzle_1 import get_invalid_ids_from_range
from puzzle_2 import get_invalid_ids_from_range


def main():
    with open('day2/puzzle_input.txt') as f:
        puzzle_input = f.read()

    input_id_ranges = puzzle_input.split(',')

    invalid_ids = []
    for id_range in  input_id_ranges:
        invalid_ids.extend(
            get_invalid_ids_from_range(id_range)
        )

    sum_of_invalid_ids = sum(invalid_ids)

    print(f"The sum of invalid ID's is: {sum_of_invalid_ids}")


if __name__ == "__main__":
    main()

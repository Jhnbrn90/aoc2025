from itertools import chain

from part_1 import (
    parse_input,
    get_fresh_ingredients_from_ranges,
)

from part_2 import merge_overlapping_ranges

def main():
    with open('day5/puzzle_input.txt') as f:
        puzzle_input = f.read()

    ranges, available_ingredients = parse_input(puzzle_input)

    fresh_ingredients = get_fresh_ingredients_from_ranges(ranges, available_ingredients)

    amount_fresh = len(fresh_ingredients)
 
    print(f"Number of fresh ingredients: {amount_fresh}")

    # Part 2
    fresh_ingredients = []

    for minimum_value, range_list in ranges.items():
        fresh_ingredients.extend(range_list)

    merged_ranges = merge_overlapping_ranges(fresh_ingredients)
    amount_of_fresh_ingredients = sum([len(r) for r in merged_ranges])

    print(f"Number of fresh ingredients: {amount_of_fresh_ingredients}")


if __name__ == "__main__":
    main()


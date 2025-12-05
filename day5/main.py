from part_1 import (
    parse_input,
    get_fresh_ingredients_from_ranges,
)


def main():
    with open('day5/puzzle_input.txt') as f:
        puzzle_input = f.read()

    ranges, available_ingredients = parse_input(puzzle_input)

    fresh_ingredients = get_fresh_ingredients_from_ranges(
        ranges,
        available_ingredients,
    )

    amount_fresh = len(fresh_ingredients)
    print(f"Number of fresh ingredients: {amount_fresh}")


if __name__ == "__main__":
    main()


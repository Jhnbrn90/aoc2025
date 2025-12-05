import time

from itertools import chain


def str_to_range(range_str: int) -> range:
    start, end = range_str.split('-')

    return range(int(start), int(end)+1)


def combine_ranges(ranges: list[range]) -> list[int]:
    """Combine ranges and return list of integers."""
    # Alternative approach
    # list_of_integers = list(chain(*ranges))
    # unique_integers = set(list_of_integers)
    # return list(unique_integers)

    set_of_integers = set()
    for single_range in ranges:
        for i in single_range:
            set_of_integers.add(i)

    return list(set_of_integers)


def get_fresh_ingredients_from_ranges(ranges: list[range], available_ingredients: list[int]) -> list[int]:
    """Retreive fresh ingredients from the available ingredients."""
    fresh_ingredients = combine_ranges(ranges)

    available_fresh_ingredients = []

    for ingredient in available_ingredients:
        if ingredient in fresh_ingredients:
            available_fresh_ingredients.append(ingredient)

    return available_fresh_ingredients


def parse_input(puzzle_input: str) -> tuple[list[range], list[int]]:
    """Convert input to list of ranges and list of available ingredients.
    ---------
        3-5
        10-14

        1
        5
        8
    ---------
    """
    ranges_str, ingredients_str = puzzle_input.split('\n\n')

    ranges_list = [str_to_range(r) for r in ranges_str.split('\n') if r != '']
    ingredients_list = [int(i) for i in ingredients_str.split('\n') if i != '']

    return ranges_list, ingredients_list

from collections import defaultdict
from itertools import chain


def range_list_to_dict(range_str_list: list[str]) -> dict[int, range]:
    """Provide dictionary of ranges with lowest value included in range as key."""
    range_dict = defaultdict(list)

    for range_str in range_str_list:
        if range_str == '':
            continue

        start, end = [int(i) for i in range_str.split('-')]
        range_dict[start].append(range(start, end+1))

    return range_dict


def get_fresh_ingredients_from_ranges(ranges: list[range], available_ingredients: list[int]) -> set[int]:
    """Retreive fresh ingredients from the available ingredients."""
    # The ranges are returned as dictionary of minimum value, followed by
    # the overlapping ranges, i.e.:
    # {3: [range(3, 6), range(3, 4)]}
    fresh_ingredients = set()
    for ingredient in available_ingredients:
        possible_ranges = [r for r in ranges if ingredient >= r]
        for possible_range in possible_ranges:
            for ingredient_range in ranges[possible_range]:
                if ingredient in ingredient_range:
                    fresh_ingredients.add(ingredient)

    return fresh_ingredients
    

def parse_input(puzzle_input: str) -> tuple[dict[int, list[range]], list[int]]:
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
    ranges_dict = range_list_to_dict(ranges_str.split('\n')) 

    ingredients_list = [int(i) for i in ingredients_str.split('\n') if i != '']

    return ranges_dict, ingredients_list

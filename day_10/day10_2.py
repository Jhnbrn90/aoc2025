from functools import cache
from collections.abc import Sequence, Set
from collections import defaultdict
from itertools import combinations


# Wiring = {1, 2, 3}
type Wiring = Set[int]

# Presses = ({1,3}, {1})
type Presses = tuple[Wiring, ...]


def parse_machine(input_str: str) -> tuple[str, list[str], str]:
    """Parse the input line into the corresponding indicators, buttons and joltages.

    Note that we're using [1:-1] slicing to strip of '{}', '()' or '[]'.
    """
    str_parts = input_str.split(' ')

    machine_part = str_parts.pop(0)  # first element ->  machine
    indicators = {i for i, character in enumerate(machine_part[1:-1]) if character == "#"}

    joltage_part = str_parts.pop()  # last element -> joltage requirements
    joltages = list(map(int, joltage_part[1:-1].split(",")))

    # `str_parts` have only the buttons as list[str] remaining
    buttons = []
    for encapsulated_button in str_parts:
        wires = encapsulated_button[1:-1].split(",")
        buttons.append(set(map(int, wires)))

    return indicators, buttons, joltages


def find_possible_button_combinations(desired_state: Wiring, buttons: list[Wiring]) -> int | None:
    for used_number_of_buttons in range(1, len(buttons) + 1):

        for button_combinations in combinations(buttons, r=used_number_of_buttons):
            indicator_pattern: Wiring = set()

            for button_press in button_combinations:
                indicator_pattern ^= button_press 

            if indicator_pattern == desired_state:
                return used_number_of_buttons
    
    return None


def minimum_presses_reaching_state(desired_state: Wiring, patterns: dict[Wiring, list[Presses]]) -> int | None:
    """Find the least amount of button presses needed to reach given state."""
    presses_list = patterns.get(frozenset(desired_state), [])
    return min((len(presses) for presses in presses_list), default=None)


def minimum_presses_reaching_joltages(target_joltages: list[int], patterns: dict[Wiring, list[Presses]]) -> int | None:
    

    @cache
    def get_minimum_presses(target_joltages: tuple[int, ...]) -> int | None:
        if not any(target_joltages):
            # if all joltages are 0, return 0
            return 0

        # The desired state should be matched by using the odd joltage levels
        indicators = frozenset(i for i, joltage in enumerate(target_joltages) if joltage %2 == 1)

        result = None

        for presses in patterns[indicators]:
            remaining_joltages = list(target_joltages)

            for button in presses:
                for idx in button:
                    remaining_joltages[idx] -= 1

            if any(joltage < 0 for joltage in remaining_joltages):
                continue
        
            # Since we've updated all the odd joltages, the remaining joltages are even
            half_remaining_joltages = tuple(joltage // 2 for joltage in remaining_joltages)
            minimum_button_presses_to_reach_half = get_minimum_presses(half_remaining_joltages)

            if minimum_button_presses_to_reach_half is None:
                continue

            # len(presses) represents the button presses to get to the indicator state (the odd values)
            # If one press gets to half of the joltages, we need to do that twice (hence "2*")
            button_presses = len(presses) + (2 * minimum_button_presses_to_reach_half)
            
            if result is None:
                # initially, `result` starts at `None`
                result = button_presses
            else:
                result = min(result, button_presses)

        return result
        
    # Make it a tuple, to support `cache()`
    return get_minimum_presses(tuple(target_joltages))





def possible_patterns(buttons: Sequence[Wiring]) -> dict[Wiring, list[Presses]]:
    """
    Precompute all possible indicator patterns and the combinations of
    button presses that produce them.
    """
    # patterns = {
    #   {1,3}: [{1,2,3}, {3}, {2}, ...],
    #   ...,
    # }
    patterns: dict[Wiring, list[Presses]] = defaultdict(list)

    # Start from the fewest presses of buttons, until pressing all the buttons
    for num_presses in range(len(buttons) + 1):
        # Find all combinations of possible buttons, at most once
        # More like: find all *sequences* of the possible buttons
        for presses in combinations(buttons, num_presses):

            pattern: Wiring = set()

            # button is a set of `int` (`Wiring`)
            for button in presses:
                pattern ^= button

            # Append the button presses leading to a certain pattern
            patterns[frozenset(pattern)].append(presses)

    return patterns

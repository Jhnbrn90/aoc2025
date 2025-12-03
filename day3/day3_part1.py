def parse_battery_string_to_bank_list(battery_bank_string: str) -> list[int]:
    """Helper function to return a list of integers from a string of integers."""
    return [int(i) for i in battery_bank_string]


def max_joltage_from_battery_bank(battery_bank: list[int]) -> int:
    """Calculate the maximum joltage provided by battery bank.

    In 987654321111111, you can make the largest joltage possible, 98,
    by turning on the first two batteries.

    Using the pointers `i` and `j`, the optimal values for the left digit
    (tens) and right digit (ones) should be found.
    
            i                        j
            3 8 7 6 9 4 3 2 1  1  1  1
    index:  0 1 2 3 4 5 6 7 8  9  10  11

            -->
                    i  <------------ j
            3 8 7 6 9 4 3 2 1  1  1  1
    index:  0 1 2 3 4 5 6 7 8  9  10  11
    """

    # We have two pointers, looking for the optimal left digit (tens) and right digit (ones)
    last_index = len(battery_bank)-1  # zero-indexed

    i = 0
    best_i = i

    while i < last_index:
        i += 1

        if i == last_index:  # i can't be located at the last index
            break
        
        current_value = battery_bank[i]
        if battery_bank[i] > battery_bank[best_i]:
            best_i = i

    # Find highest value for j
    j = last_index  
    best_j = j

    while j > best_i:
        j -= 1
        if j == best_i:  # j can't be located at index of `i`
            break

        current_value = battery_bank[j]
        if battery_bank[j] > battery_bank[best_j]:
            best_j = j

    return int(str(battery_bank[best_i]) + str(battery_bank[best_j]))

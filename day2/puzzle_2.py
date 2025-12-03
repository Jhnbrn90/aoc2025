def single_digit_repeat(id_string: str) -> bool:
    """Determine if the ID contains a single repeated digit.

    ID:      [ 1  1  1  1 ]
    i:         0  1  2  3

    lenght: 4
    range(0, 4-1) --> 0, 1, 2
    range comparison:
      - str[0] == str[1]
      - str[1] == str[2]
      - str[2] == str[3]
    """
    if len(id_string) <= 1:
        return False

    for i in range(0, len(id_string)-1):  # one less in range, to compare with next
        if not id_string[i] == id_string[i+1]:
            return False

    return True


def get_prime_factors(id_size: int) -> list[int]:
    """Get the prime factors for a given input integer.

    This will result in all possible combinations of groups
    to determine the possible repeated digit combinations.
    """
    groups = set()

    for group_size in range(2, id_size):  # this excludes upper `id_size` (single group)
        if id_size % group_size == 0:
            # if the ID length is cleanly divisible by this group size it is valid
            groups.add(group_size)

    return groups


def get_invalid_ids_from_range(input_range: str):
    invalid_ids: list[int] = []
    start, end = input_range.split('-')
    start_int, end_int = int(start), int(end)

    for id_as_int in range(start_int, end_int + 1):  # range is exclusive
       id_as_str = str(id_as_int)
       id_length = len(id_as_str)

       # All ID's having length 1 can't have repeated silly patterns
       if id_length <= 1:
           continue

       # Scenario 1 - Single repeated digit ('111')
       if single_digit_repeat(id_as_str):
           invalid_ids.append(id_as_int)
           continue

       # Scenario 2 - The ID has an even number of digits
       ## Check if the largest element is simply repeated
       if len(id_as_str) % 2 == 0:
           middle_slice_index = id_length // 2

           #         [ 1 | 0 | 1 | 0 ]
           # slice:  0   1   2   3   4
           first_part = id_as_str[0:middle_slice_index]
           second_part = id_as_str[middle_slice_index:]

           if first_part == second_part:
               invalid_ids.append(id_as_int)
               continue

       # Scenario 4 - ID has multiple repeated fragments
       # Find the fragments, for example: [565656] or [123123123]

       # To find the possible group sizes, get all prime factors
       # for the length of the ID. An ID of size 6, can have:
       #  - groups of size 2 (3 x 2 = 6)
       #  - groups of size 3 (2 x 3 = 6)
       possible_group_sizes = get_prime_factors(id_length)

       for group_size in possible_group_sizes:
           repeated_element = id_as_str[0:group_size]  # '56' or '123'

           repeated_expected_id_string = repeated_element * (id_length // group_size)

           if repeated_expected_id_string == id_as_str:
               invalid_ids.append(id_as_int)
               break

    return invalid_ids

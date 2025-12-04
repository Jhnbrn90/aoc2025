def list_batteries_to_joltage(battery_list: list[int]) -> int:
    """Helper function to convert selected batteries to maximum joltage output.

    For example, [ 1, 2, 3 ] should yield 123 as the joltage.
    """
    return int(''.join([str(i) for i in battery_list]))


def get_index_for_highest_joltage(battery_bank: list[int]):
    """Return highest index value for first entry with highest joltage.

    From left to right, so [ 9, 9, 9, 8] will return index 0.
    """

    i = 0

    max_index = i

    while i < len(battery_bank)-1:
        i+= 1

        if battery_bank[i] > battery_bank[max_index]:
            max_index = i

    return max_index


def get_selection_window(battery_bank: list[int], amount_to_select: int):
    """Return windowed view of the current battery bank.

    If we were to select 4 batteries from a list of 5:
    [ 2, 1, 3, 4, 0 ]


    In this case, we want to select from the "2" and "1" and leave the 3
    other batteries, to add up to a total  of 4 batteries.

    In this case, this function would return a 'selection window' of:
    [ 2, 1 ]
    """
    # After selection of 1 battery, We should leave enough options open to
    # add up to the amount to select
    minimal_left_over = amount_to_select - 1
    window_range = len(battery_bank) - minimal_left_over
    selection_window = battery_bank[0:window_range]

    return selection_window


def select_index_using_window(battery_bank: list[int], amount_to_select: int):
    """Return highest index value within a given window.

    If we were to select 4 batteries from a list of 5:
    [ 2, 1, 3, 4, 0 ]

    In this case, we should first select the left-most digit from a window
    that leaves enough entries to end up with a total of 4 batteries. This leaves
    2 and 1 to choose from and should "preserve" 3 4 and 0.
    """
    selection_window = get_selection_window(battery_bank, amount_to_select)
    highest_index = get_index_for_highest_joltage(selection_window)

    return highest_index

    
def select_batteries_from(battery_bank: list[int], amount_to_select: [int]):
    battery_joltages = []

    for to_select in reversed(range(1, amount_to_select+1)):
        highest_index = select_index_using_window(battery_bank, to_select)
        battery_joltages.append(battery_bank[highest_index])
        battery_bank = battery_bank[highest_index+1:]  # discard all values left of highest index

    return battery_joltages

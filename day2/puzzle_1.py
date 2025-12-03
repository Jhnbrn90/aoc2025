def get_invalid_ids_from_range(input_range: str):
    invalid_ids: list[int] = []
    start, end = input_range.split('-')
    start_int, end_int = int(start), int(end)

    for id_as_int in range(start_int, end_int + 1):  # range is exclusive
       id_as_str = str(id_as_int)

       # Check if the ID might contain a central pivot
       # point to repeat the number, for example '1010', but
       # not '101'.
       if len(id_as_str) % 2 == 0:
           # Calculate center of this ID
           middle_slice_index = len(id_as_str) // 2

           #         [ 1 | 0 | 1 | 0 ]
           # slice:  0   1   2   3   4
           first_part = id_as_str[0:middle_slice_index]
           second_part = id_as_str[middle_slice_index:]

           if first_part == second_part:
               invalid_ids.append(id_as_int)

    return invalid_ids

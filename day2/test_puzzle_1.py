import pytest

from puzzle_1 import get_invalid_ids_from_range


@pytest.mark.parametrize('input_range,expected_invalid_ids', [
    ('11-22', [11, 22]),
    ('95-115', [99]),
    ('998-1012', [1010]),
    ('1188511880-1188511890', [1188511885]),
    ('222220-222224', [222222]),
    ('1698522-1698528', []),
    ('446443-446449', [446446]),
    ('38593856-38593862', [38593859]),
])
def test_get_invalid_ids_for_range(input_range, expected_invalid_ids):
    result = get_invalid_ids_from_range(input_range)
    assert result == expected_invalid_ids


def test_parse_input_ids():
    with open('sample_input.txt') as f:
        puzzle_input = f.read()

    input_id_ranges = puzzle_input.split(',')

    invalid_ids = []
    for id_range in  input_id_ranges:
        invalid_ids.extend(
            get_invalid_ids_from_range(id_range)
        )

    assert invalid_ids == [
        11,
        22,
        99,
        1010,
        1188511885,
        222222,
        446446,
        38593859,
    ]

    assert sum(invalid_ids) == 1227775554

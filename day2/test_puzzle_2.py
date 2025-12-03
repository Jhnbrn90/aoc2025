import pytest

from puzzle_2 import (
    get_prime_factors,
    get_invalid_ids_from_range,
    single_digit_repeat,
)


@pytest.mark.parametrize('input_id,is_repeated', [
    ('99', True),
    ('999', True),
    ('111', True),
    ('11', True),
    ('22222222222', True),
    ('333333', True),
    ('4444', True),
    ('4', False),
    ('1010', False),
])
def test_single_digit_repeat(input_id: str, is_repeated: bool):
    """Check it can determine if ID has single repeated digit."""
    assert single_digit_repeat(input_id) is is_repeated


def test_group_sizes():
    result = get_prime_factors(6)
    assert result == {2, 3}


@pytest.mark.parametrize('input_range,expected_invalid_ids', [
    ('11-22', [11, 22]),
    ('95-115', [99, 111]),
    ('998-1012', [999, 1010]),
    ('1188511880-1188511890', [1188511885]),
    ('222220-222224', [222222]),
    ('1698522-1698528', []),
    ('446443-446449', [446446]),
    ('38593856-38593862', [38593859]),
    ('824824821-824824827', [824824824]),
    ('2121212118-2121212124', [2121212121]),
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
        111,
        999,
        1010,
        1188511885,
        222222,
        446446,
        38593859,
        565656,
        824824824,
        2121212121
    ]

    assert sum(invalid_ids) == 4174379265

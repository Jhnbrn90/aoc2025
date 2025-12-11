import pytest

from day11_1 import (
    get_device_map,
    DeviceMap,
)


DEVICE_MAP = {
    "aaa": ("you", "hhh"),
    "you": ("bbb", "ccc"),
    "bbb": ("ddd", "eee"),
    "ccc": ("ddd", "eee", "fff"),
    "ddd": ("ggg",),
    "eee": ("out",),
    "fff": ("out",),
    "ggg": ("out",),
    "hhh": ("ccc", "fff", "iii"),
    "iii": ("out",),
}

def test_dict_of_devices():
    with open('day_11/sample_input.txt') as f:
        puzzle_input = f.read().strip()

    assert get_device_map(puzzle_input) == DEVICE_MAP 


@pytest.mark.parametrize('device,expected_paths', [
   ('aaa', ("you", "hhh")),
   ('ccc', ("ddd", "eee", "fff")),
   ('fff', ("out",)),
])
def test_get_paths(device: str, expected_paths: tuple[str]):
    assert DEVICE_MAP.get(device) == expected_paths


def test_sample_input():
    device_map_instance = DeviceMap(DEVICE_MAP)
    device_map_instance.follow_path('you')
    assert device_map_instance.paths == 5

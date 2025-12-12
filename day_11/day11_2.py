from functools import cache
from typing import Callable


def make_find_paths_fn(device_map: dict[str, tuple[str]]) -> Callable:
    @cache
    def find_paths(current, target):
        if current == target:
            return 1
        
        return sum(
            find_paths(connected_device, target)
            for connected_device in device_map[current]
        )

    return find_paths

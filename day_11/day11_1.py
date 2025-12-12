from collections import defaultdict


def get_device_map(device_input: str) -> dict[str, tuple]:
    device_map = defaultdict(tuple)

    for device_line in device_input.split("\n"):
        elements = device_line.split(' ')
        device_map[elements[0].strip(':')] = tuple(elements[1:])

    return device_map


class DeviceMap:
    def __init__(self, device_map: dict[str, tuple]):
        self.device_map = device_map
        self.paths = 0

    def follow_path(self, device: str) -> None:
        for dev in self.device_map.get(device):
            if dev == "out":
                self.paths += 1
                continue

            self.follow_path(dev)


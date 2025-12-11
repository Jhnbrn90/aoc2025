from day11_1 import (
    get_device_map,
    DeviceMap,
)


def main():
    with open('day_11/puzzle_input.txt') as f:
        puzzle_input = f.read().strip()

    device_map_dict = get_device_map(puzzle_input)
    device_map_instance = DeviceMap(device_map_dict)
    device_map_instance.follow_path('you')

    print(f"Paths: {device_map_instance.paths}")



if __name__ == "__main__":
    main()



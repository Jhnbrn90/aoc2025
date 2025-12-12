from day11_1 import get_device_map
from day11_2 import make_find_paths_fn


def main():
    with open('day_11/puzzle_input.txt') as f:
        puzzle_input = f.read().strip()

    device_map = get_device_map(puzzle_input)

    # Create a cached `find_paths` function, using `device_map`
    find_paths = make_find_paths_fn(device_map)

    # Day 1
    total = find_paths('you', 'out')

    print(f"Day 1: {total}")

    # Day 2
    total = 0

    # Route 1 - SVR > DAC > FFT > OUT
    total += find_paths('svr', 'dac') * find_paths('dac', 'fft') * find_paths('fft', 'out')
    
    # Route 2 - SVR > FFT > DAC > OUT
    total += find_paths('svr', 'fft') * find_paths('fft', 'dac') * find_paths('dac', 'out')

    print (f"Day 2: {total}")


if __name__ == "__main__":
    main()



from day9_1 import (
    Tile,
    largest_euclidian_distances,
    find_largest_area_n_distances,
)


def main():
    with open('day9/puzzle_input.txt') as f:
        puzzle_input = f.read()

    input_coordinates = [c for c in puzzle_input.split("\n") if c != '']

    coordinates = []
    for line in input_coordinates:
        x, y = line.split(",")
        coordinates.append(Tile(x=int(x), y=int(y)))

    distances = largest_euclidian_distances(coordinates)
    largest_area = find_largest_area_n_distances(n=10000, distances=distances, tiles=coordinates)


    print(f"Day9|1: largest area: {largest_area}")


if __name__ == "__main__":
    main()

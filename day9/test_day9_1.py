from day9_1 import (
    Tile,
    largest_euclidian_distances,
    find_largest_area_n_distances,)


def test_largest_euclidian_distances():
    with open('day9/sample_input.txt') as f:
        puzzle_input = f.read()

    input_coordinates = [c for c in puzzle_input.split("\n") if c != '']

    coordinates = []
    for line in input_coordinates:
        x, y = line.split(",")
        coordinates.append(Tile(x=int(x), y=int(y)))

    distances = largest_euclidian_distances(coordinates)

    assert distances == [
        (97, (2, 6)),
        (97, (1, 5)),
        (85, (2, 5)),
        (85, (1, 6)),
        (65, (3, 6)),
        (53, (4, 6)),
        (53, (3, 5)),
        (52, (0, 2)),
        (49, (4, 5)),
        (41, (0, 5)),
        (40, (1, 3)),
        (40, (0, 3)),
        (36, (1, 2)),
        (32, (2, 7)),
        (29, (5, 7)),
        (29, (0, 6)),
        (25, (6, 7)),
        (20, (3, 7)),
        (20, (1, 7)),
        (20, (1, 4)),
        (20, (0, 4)),
        (16, (0, 1)),
        (8, (4, 7)),
        (8, (2, 4)),
        (4, (5, 6)),
        (4, (3, 4)),
        (4, (2, 3)),
        (4, (0, 7))
    ] 


def test_get_largest_areas_for_n_largest_distances():
    with open('day9/sample_input.txt') as f:
        puzzle_input = f.read()

    input_coordinates = [c for c in puzzle_input.split("\n") if c != '']

    coordinates = []
    for line in input_coordinates:
        x, y = line.split(",")
        coordinates.append(Tile(x=int(x), y=int(y)))

    distances = largest_euclidian_distances(coordinates)

    largest_area = find_largest_area_n_distances(n=10, distances=distances, tiles=coordinates)

    assert largest_area == 50

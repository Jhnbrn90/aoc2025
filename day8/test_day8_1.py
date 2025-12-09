import math

from day8_1 import (
    calculate_squared_distance,
    connect_n_shortest_distances,
    get_n_largest_circuits,
    Node,
    node_list_to_distances,
    parse_list_of_coordinates_to_node_list,
)


def test_calculate_squared_euclidian_distance():
    p = Node(
        x=162,
        y=817,
        z=812,
    )

    q = Node(
        x=425,
        y=690,
        z=689,
    )

    expected_distance = 100427
    assert calculate_squared_distance(p, q) == expected_distance


def test_node_has_coordinates():
    p = Node(x=1, y=2, z=3)
    assert p.x == 1
    assert p.y == 2
    assert p.z == 3


def test_sort_by_distance():
    with open('day8/sample_input.txt') as f:
        puzzle_input = f.read()

    node_list = parse_list_of_coordinates_to_node_list(puzzle_input)
    distances = node_list_to_distances(node_list)

    assert distances[0] == (100427, (0, len(node_list)-1))


def test_connect_n_shortest_distances():
    with open('day8/sample_input.txt') as f:
        puzzle_input = f.read()

    node_list = parse_list_of_coordinates_to_node_list(puzzle_input)

    # Sorted list of distances
    distances = node_list_to_distances(node_list)

    # Perform the connections
    circuits = connect_n_shortest_distances(
        n=1,
        node_list=node_list,
        distances=distances
    )

    # A circuit is formed between node 19 and 0: circuit 0
    assert circuits == {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 0,
    }


def test_calculate_n_largest_circuits():
    with open('day8/sample_input.txt') as f:
        puzzle_input = f.read()

    node_list = parse_list_of_coordinates_to_node_list(puzzle_input)

    # Sorted list of distances
    distances = node_list_to_distances(node_list)

    # Perform the connections
    circuits = connect_n_shortest_distances(
        n=10,
        node_list=node_list,
        distances=distances
    )

    largest_circuits = get_n_largest_circuits(n=3, circuits=circuits)

    assert largest_circuits == [
        (2, 5),
        (14, 4),
        (9, 2),
    ]

    assert math.prod([size for _, size in largest_circuits]) == 40

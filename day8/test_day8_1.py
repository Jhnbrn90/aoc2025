from day8_1 import (
    calculate_squared_distance,
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

    assert distances[0] == (100427, (node_list[0], node_list[-1]))


def test_calculate_circuits():
    with open('day8/sample_input.txt') as f:
        puzzle_input = f.read()

    node_list = parse_list_of_coordinates_to_node_list(puzzle_input)
    distances = node_list_to_distances(node_list)

    circuits = {i: i for i, node in enumerate(node_list)}

    for n, (distance, (node1, node2)) in enumerate(distances):


        if n == 1000:
            break

    return

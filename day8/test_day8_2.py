from day8_1 import (
    parse_list_of_coordinates_to_node_list,
    node_list_to_distances,
)

from day8_2 import (
    connect_everything,
)


def test_connect_until_single_circuit():
    with open('day8/sample_input.txt') as f:
        puzzle_input = f.read()

    node_list = parse_list_of_coordinates_to_node_list(puzzle_input)

    # Sorted list of distances
    distances = node_list_to_distances(node_list)

    # Perform the connections and get indexes of the remaining nodes
    i, j = connect_everything(
        node_list=node_list,
        distances=distances
    )

    # Calculate the answer
    assert node_list[i].x == 216
    assert node_list[j].x == 117
    node_list[i].x * node_list[j].x == 25272

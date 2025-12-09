import math

from day8_1 import (
    parse_list_of_coordinates_to_node_list,
    node_list_to_distances,
    connect_n_shortest_distances,
    get_n_largest_circuits,
)


from day8_2 import (
    connect_everything,
)


def main():
    with open('day8/puzzle_input.txt') as f:
        puzzle_input = f.read()

    node_list = parse_list_of_coordinates_to_node_list(puzzle_input)

    # Sorted list of distances
    distances = node_list_to_distances(node_list)

    # Perform the connections
    circuits = connect_n_shortest_distances(
        n=1000,
        node_list=node_list,
        distances=distances
    )

    largest_circuits = get_n_largest_circuits(n=3, circuits=circuits)

    product_of_largest = math.prod([size for _, size in largest_circuits])

    print(f"Day 1: largest circuits multiplied: {product_of_largest}.")

    # Day 2- perform the connections and get indexes of the remaining nodes
    i, j = connect_everything(
        node_list=node_list,
        distances=distances
    )

    # Calculate the answer
    product_x_remaining_nodes = node_list[i].x * node_list[j].x

    print(f"Day 2: remaining node x's multiplied: {product_x_remaining_nodes}")


if __name__ == "__main__":
    main()

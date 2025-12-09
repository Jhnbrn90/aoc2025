from collections import Counter
from dataclasses import dataclass


@dataclass
class Node:
    """Represent a junction box."""
    x: int
    y: int
    z: int


def calculate_squared_distance(p: Node, q: Node):
    """Return squared euclidian distance between nodes.

    For 3D coordinates (x,y,z), the Euclidian distance can be
    calculated as: sqrt((qx-px)^2 + (qy-py)^2 + (qz - pz)^2).

    The squared distance is returned from this function for
    performance reasons. If the non-squared distance is required,
    it should be manually calculated with `math.sqrt()`.
    """
    return (q.x-p.x)**2 + (q.y-p.y)**2 + (q.z-p.z)**2


def parse_list_of_coordinates_to_node_list(input_list: list[str]) -> list[Node]:
    """Provide list of `Node` objects from the list of input coordinates."""
    node_list = []

    for node in input_list.strip().split("\n"):
        x, y, z = node.split(",")
        node_list.append(
            Node(
                x=int(x),
                y=int(y),
                z=int(z)
            )
        )

    return node_list


def node_list_to_distances(node_list: list[Node]) -> list[tuple[int, tuple[int, int]]]:
    """Return node distances sorted on closest distance."""
    distances = []  # list of tuple of (distance, (node1, node2))

    for i, node in enumerate(node_list):
        if i == len(node_list)-1:
            break

        # Calculate all the distances from the node_list for this point
        for j in range(i+1, len(node_list)):
            # Store tuples of distance and node indexes
            distances.append(
                (calculate_squared_distance(node_list[i], node_list[j]), (i, j))
            )

    return sorted(distances)


def connect_n_shortest_distances(n: int, node_list: list[Node], distances: list[tuple[int, tuple[int, int]]]) -> dict[int, int]:
    """Provide mapping of nodes to circuits, after connecting the `n` shortest nodes."""
    # Map of nodes and to which circuit they belong to
    circuit_map = {i: i for i, _ in enumerate(node_list)}

    # Creating the connections, limited by `n`
    for distance, (node_i, node_j) in distances[:n]:
        # Scenario 1 - Both nodes are not belonging to a bigger circuit
        if circuit_map[node_i] == node_i and circuit_map[node_j] == node_j:
            # Update node_j to become part of the circuit of node_i
            circuit_map[node_j] = circuit_map[node_i]

        # Scenario 2 - Both nodes are already part of the same circuit
        if circuit_map[node_i] == circuit_map[node_j]:
            # Do nothing
            continue
        
        # Scenario 3 - One or both nodes are part of another circuit
        circuit_of_node_i = circuit_map[node_i]
        circuit_of_node_j = circuit_map[node_j]
        if circuit_of_node_i != node_i or circuit_of_node_j != node_j:
            # All nodes become members of the same circuit
            # Get all nodes of the circuit of j, and make them member of the circuit of node_i
            # {1:1, 2:1, 3:1, 4: 5, 5: 5, 6:5}
            
            target_circuit = circuit_map[node_j]
            for node_index, circuit in circuit_map.items():
                if circuit == target_circuit:
                    circuit_map[node_index] = circuit_map[node_i]

    return circuit_map


def get_n_largest_circuits(n: int, circuits: dict[int, int]) -> list[tuple[int, int]]:
    """Find and return the `n` largest circuits."""
    circuit_sizes = [x for x in circuits.values()]
    return Counter(circuit_sizes).most_common(n)

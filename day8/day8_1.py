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


def node_list_to_distances(node_list: list[Node]) -> list[tuple[int, tuple[Node, Node]]]:
    """Return node distances sorted on closest distance."""
    distances = []  # list of tuple of (distance, (node1, node2))

    for i, node in enumerate(node_list):
        if i == len(node_list)-1:
            break

        # Calculate all the distances from the node_list for this point
        for j in range(i+1, len(node_list)):
            next_node = node_list[j]

            distances.append(
                (calculate_squared_distance(node, next_node), (node, next_node))
            )

    return sorted(distances)

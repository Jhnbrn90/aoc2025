from day8_1 import (
    Node,
)


def connect_everything(node_list: list[Node], distances: list[tuple[int, tuple[int, int]]]) -> tuple[int, int]:
    """Provide the indexes of the remaining nodes after connecting everything."""
    # Map of nodes and to which circuit they belong to
    circuit_map = {i: i for i, _ in enumerate(node_list)}

    # Creating the connections, limited by `n`
    for distance, (node_i, node_j) in distances:
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

        # Check to see if we have obtained a single circuit, containing all nodes
        if len(set(circuit_map.values())) == 1:
            # If so, the remaining nodes i and j are the last ones that need to be
            # connected to the wall
            return node_i, node_j

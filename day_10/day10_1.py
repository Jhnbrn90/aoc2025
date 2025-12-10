from functools import cached_property


def parse_input_str_to_parts(input_str: str) -> tuple[str, list[str]]:
    str_parts = input_str.split(' ')

    machine_part = str_parts.pop(0)  # first element ->  machine
    joltage_part = str_parts.pop()  # last element -> joltage requirements

    return machine_part, str_parts


class Machine:
    def __init__(self, desired_state: str):
        self.desired_state_str = desired_state

    @cached_property
    def desired_state(self):
        # Remove '[' and ']'
        desired_state = self.desired_state_str[1:-1]
        desired_state = desired_state.replace('#', '1')
        desired_state = desired_state.replace('.', '0')
        return desired_state


def apply_xor_to(current_state: str, operation: str):
    result = int(current_state, 2) ^ int(operation, 2)
    return bin(result)[2:]  # skip '0b'


from collections import defaultdict
from functools import cache, cached_property
from itertools import permutations



def parse_input_str_to_parts(input_str: str) -> tuple[str, list[str]]:
    str_parts = input_str.split(' ')

    machine_part = str_parts.pop(0)  # first element ->  machine
    joltage_part = str_parts.pop()  # last element -> joltage requirements

    # `str_parts` have only the buttons as list[str] remaining
    return machine_part, str_parts


@cache
def apply_xor_to(current_state: str, operation: str):
    result = int(current_state, 2) ^ int(operation, 2)
    return bin(result)[2:]  # skip '0b'


@cache
def button_to_binary(n_buttons: int, button_str: str) -> str:
    """Return binary representation of button."""
    representation = ['0'] * n_buttons

    # Convert (0,3) in a list of [0, 3]
    wires = list(map(int, button_str[1:-1].split(',')))

    for i in wires:
        representation[i] = '1'

    return ''.join(representation)



class Machine:
    def __init__(self, desired_state: str):
        self.desired_state_str = desired_state
        # All machines start having all lights off
        self.current_state = '0' * len(self.desired_state)
        self.pushed_buttons = []

    @cached_property
    def desired_state(self):
        # Remove '[' and ']'
        desired_state = self.desired_state_str[1:-1]
        desired_state = desired_state.replace('#', '1')
        desired_state = desired_state.replace('.', '0')
        return desired_state

    def reset(self):
        self.current_state = '0' * len(self.desired_state)
        self.pushed_buttons = []

    def push_button(self, button: str):
        self.pushed_buttons.append(button)
        button_operation = button_to_binary(
            n_buttons=len(self.current_state),
            button_str=button,
        )

        # Perform XOR binary operation on current state
        new_state = apply_xor_to(self.current_state, button_operation)

        # Calculate padding if necessary
        padding = '0' * (len(self.current_state) - len(new_state))
        self.current_state = padding + new_state


def find_shortest_path(machine: Machine, buttons: list[str]):
    # For all the possible permutations of pushing the buttons
    button_presses_reaching_desired_state = defaultdict(list)

    for i, permutation in enumerate(permutations(buttons)):
        # # If we've reached a desired state already
        # if button_presses_reaching_desired_state:
        #     # Skip the permutation if the first n buttons already
        #     # reached the desired state, since we can't end up with
        #     # less button presses.
        #     current_minimum = min(list(map(len, button_presses_reaching_desired_state)))
        #     if list(permutation[:current_minimum]) in button_presses_reaching_desired_state:
        #         print(f'Skipping permutation: {permutation}')
        #         continue
        for button in permutation:
            machine.push_button(button)

            if machine.current_state == machine.desired_state:
                buttons_pressed = machine.pushed_buttons
                n_buttons_pressed = len(buttons_pressed)
                button_presses_reaching_desired_state[n_buttons_pressed].append(buttons_pressed)
                machine.reset()
                break

    return min(button_presses_reaching_desired_state.keys())

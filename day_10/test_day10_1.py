import pytest

from itertools import permutations

from day10_1 import (
    button_to_binary,
    parse_input_str_to_parts,
    Machine,
    apply_xor_to,
)


@pytest.mark.parametrize('input_str,machine,buttons', [
    ('[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}', '[.##.]', ['(3)', '(1,3)', '(2)', '(2,3)', '(0,2)', '(0,1)']),
])
def test_parse_input_str_to_parts(input_str: str, machine: str, buttons: list[str]):
    result = parse_input_str_to_parts(input_str)
    
    assert result == (machine, buttons)


def test_machine_instance_desired_state():
    # Given we have a certain machine input string
    machine_input_str = '[.##.]'

    # When we instantiate the machine class
    machine = Machine(machine_input_str)

    # When we ask the desired state, it should match
    # the binary representation
    assert machine.desired_state == '0110'


def test_machine_instance_current_state():
    machine = Machine('[.##.]')

    # The initial state of all machines is "everything off"
    assert machine.current_state == '0000'


def test_button_to_binary_representation():
    # Given we have a string representation of a button
    button_str = '(0, 2, 5)'
    # and we have a machine that has 10 buttons
    n_buttons = 10

    # When we retrieve the binary representation
    binary_representation = button_to_binary(n_buttons, button_str)

    # The following representation is expected
    expected = '1010010000'
    assert binary_representation == expected


def test_machine_alter_state_using_button():
    machine = Machine('[.##.]')
    assert machine.current_state == '0000'

    machine.push_button('(1, 3)')

    assert machine.current_state == '0101'


def test_apply_binary_xor():
    current_state = '0110'
    # add a class for the Machine (state?)

    operation = '1111'
    result = apply_xor_to(current_state, operation)
    
    assert result == '1001'


def test_find_shortest_path_to_desired_state():
    # Given that we have an input string
    input_str = '[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}'

    # When we prepare the machine
    machine_str, buttons = parse_input_str_to_parts(input_str) 
    machine = Machine(machine_str)

    # For all the possible permutations of pushing the buttons
    buttons_reaching_desired_state = []

    for permutation in permutations(buttons):
        buttons_pressed_permutation = []
        for button in permutation:
            buttons_pressed_permutation.append(button)
            machine.push_button(button)
            if machine.current_state == machine.desired_state:
                buttons_reaching_desired_state.append(buttons_pressed_permutation)
                print(f"Reached end state, using {len(buttons_pressed_permutation)} button presses.")
                machine.reset()
                break

    assert False, buttons_reaching_desired_state

import pytest


from day10_1 import (
    button_to_binary,
    parse_input_str_to_parts,
    Machine,
    apply_xor_to,
    find_shortest_path,
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


@pytest.mark.parametrize('button,expected_state', [
    ('(1, 3)', '0101'),
    ('(3)', '0001'),
])
def test_machine_alter_state_using_button(button: str, expected_state: str):
    machine = Machine('[.##.]')
    assert machine.current_state == '0000'

    machine.push_button(button)

    assert machine.current_state == expected_state


@pytest.mark.parametrize('current_state,operation,expected', [
    ('0110', '1111', '1001'),
    ('0000', '0001', '0001'),
])
def test_apply_binary_xor(current_state: str, operation: str, expected: str):
    result = apply_xor_to(current_state, operation)
    
    assert result == expected


def test_find_shortest_path_to_desired_state():
    # Given that we have an input string
    input_str = '[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}'

    # When we prepare the machine
    machine_str, buttons = parse_input_str_to_parts(input_str)
    machine = Machine(machine_str)

    assert find_shortest_path(machine, buttons) == 2


def test_sample_input_shortest_path():
    with open(f'day_10/sample_input.txt') as f:
        puzzle_input = f.read().strip()

    total_min_path = 0
    for machine_input in puzzle_input.split("\n"):
        machine_str, buttons = parse_input_str_to_parts(machine_input)

        machine = Machine(machine_str)

        total_min_path += find_shortest_path(machine, buttons)

    assert total_min_path == 2 + 3 + 2


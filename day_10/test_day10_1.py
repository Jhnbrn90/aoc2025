import pytest


from day10_1 import (
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


def test_machine_instance_internal_state():
    # Given we have a certain machine input string
    machine_input_str = '[.##.]'

    # When we instantiate the machine class
    machine = Machine(machine_input_str)

    # When we ask the desired state, it should match
    # the binary representation
    assert machine.desired_state == '0110'


def test_apply_binary_xor():
    current_state = '0110'
    # add a class for the Machine (state?)

    operation = '1111'
    result = apply_xor_to(current_state, operation)
    
    assert result == '1001'


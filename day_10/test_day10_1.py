import pytest


def parse_input_str_to_parts(input_str: str) -> tuple[str, list[str]]:
    str_parts = input_str.split(' ')

    machine_part = str_parts.pop(0)  # first element ->  machine
    joltage_part = str_parts.pop()  # last element -> joltage requirements

    return machine_part, str_parts


@pytest.mark.parametrize('input_str,machine,buttons', [
    ('[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}', '[.##.]', ['(3)', '(1,3)', '(2)', '(2,3)', '(0,2)', '(0,1)']),
])
def test_parse_input_str_to_parts(input_str: str, machine: str, buttons: list[str]):
    result = parse_input_str_to_parts(input_str)
    
    assert result == (machine, buttons)

def test_parse_machine_and_buttons_to_binary():
    input_str = '[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}'

    machine, buttons = parse_input_str_to_binary(input_str)

    assert machine == '0110'
    assert buttons == [
        '0001',
    ]



def apply_xor_to(current_state: str, operation: str):
    result = int(current_state, 2) ^ int(operation, 2)
    return bin(result)[2:]  # skip '0b'

def test_apply_binary_xor():
    current_state = '0110'
    # add a class for the Machine (state?)

    operation = '1111'
    result = apply_xor_to(current_state, operation)
    
    assert result == '1001'


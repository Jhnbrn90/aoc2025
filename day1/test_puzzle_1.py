from puzzle_1 import VaultDial, parse_instruction


def test_vault_dial_initial_position():
    """Check that vault dial has an initial position."""
    # When no default value is provided
    vault_dial = VaultDial()
    assert vault_dial.current_position == 50

    # When a default value is provided
    vault_dial = VaultDial(initial_position=82)
    assert vault_dial.current_position == 82


def test_vault_dial_turn_right():
    vault_dial = VaultDial(0)
    assert vault_dial.current_position == 0

    vault_dial.turn_right(10)
    assert vault_dial.current_position == 10


def test_vault_dial_turn_left():
    vault_dial = VaultDial(20)
    assert vault_dial.current_position == 20

    vault_dial.turn_left(5)
    assert vault_dial.current_position == 15


def test_vault_dial_turn_right_overflow():
    # Given that we are at the highest number of the dial
    vault_dial = VaultDial(99)

    # When we turn right by a distance of one
    vault_dial.turn_right(1)

    # The vault dial should wrap around
    assert vault_dial.current_position == 0


def test_vault_dial_turn_left_overflow():
    # Given that we are at the highest number of the dial
    vault_dial = VaultDial(0)

    # When we turn right by a distance of one
    vault_dial.turn_left(1)

    # The vault dial should wrap around
    assert vault_dial.current_position == 99


def test_vault_dial_record_passed_numbers():
    # Given that we have a vault dial
    vault_dial = VaultDial(15)

    # When we turn it left and right a couple of times
    vault_dial.turn_left(1)  # 14
    vault_dial.turn_right(10)  # 24
    vault_dial.turn_left(25)  # 99

    # It should have recorded all values it stopped at
    assert vault_dial.recorded_stops == [14, 24, 99]


def test_parse_instruction_string():
    instruction_str_left = 'L86'
    instruction_str_right = 'R100'

    assert parse_instruction(instruction_str_left) == -86
    assert parse_instruction(instruction_str_right) == 100


def test_turn_dial_string_input():
    # Given that we have a vault dial
    vault_dial = VaultDial(15)
    vault_dial.turn('L15')
    assert vault_dial.current_position == 0


def test_turn_dial_multiple_string_sequence():
    # Given that we have a vault dial
    vault_dial = VaultDial(15)

    # When we provide a series of instructions
    instructions = [
        'L15',  # 0
        'R12',  # 12
        'R3',  # 15
        'L2',  # 13
    ]

    vault_dial.turn_sequence(instructions)

    assert vault_dial.current_position == 13
    assert vault_dial.recorded_stops == [
        0,
        12,
        15,
        13,
    ]


def test_parse_sample_input():
    with open('day1/sample_input.txt') as f:
        puzzle_input = [line for line in f.read().split('\n') if line != '']

    vault_dial = VaultDial(50)
    vault_dial.turn_sequence(puzzle_input)

    assert vault_dial.recorded_stops == [
        82,
        52,
        0,
        95,
        55,
        0,
        99,
        0,
        14,
        32,
    ]

    # The number of zero's in the recorded numbers
    # the dial stopped at, i.e. 'the password'
    assert vault_dial.recorded_stops.count(0) == 3

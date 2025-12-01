from puzzle_1 import VaultDial


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

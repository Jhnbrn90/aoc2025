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

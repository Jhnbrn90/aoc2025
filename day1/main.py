from puzzle_1 import VaultDial

def main():
    with open('day1/puzzle_input.txt') as f:
        puzzle_input = [line for line in f.read().split('\n') if line != '']

    vault_dial = VaultDial(50)
    vault_dial.turn_sequence(puzzle_input)

    stopped_at_zero = vault_dial.recorded_stops.count(0)
    passed_zero = vault_dial.passed_zeros

    print(f"The dial stopped at 0 this many times: {stopped_at_zero}")
    print(f"The dial passed 0 this many times: {passed_zero}")


if __name__ == "__main__":
    main()

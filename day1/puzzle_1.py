def parse_instruction(instruction: str) -> tuple[str, int]:
    return instruction[0], int(instruction[1:])


class VaultDial:
    def __init__(self, initial_position: int = 50):
        self.current_position = initial_position
        self.start = 0
        self.end = 99
        self.number_of_dials = len(
            range(self.start, self.end + 1)  # range() is exclusive of highest
        )
        self.recorded_stops: list[int] = []
        self.passed_zeros = 0

    def turn(self, instruction: str):
        direction, distance = parse_instruction(instruction)
        match direction:
            case 'L': self.turn_left(distance)
            case 'R': self.turn_right(distance)
            case _: raise ValueError(f'Unknown direction: {direction}.')

    def turn_sequence(self, instructions: list[str]):
        for instruction in instructions:
            self.turn(instruction)

    def turn_right(self, distance: int):
        new_position_sum = self.current_position + distance
        new_position = new_position_sum % self.number_of_dials

        # Given we start at '99' and move  'R1', the new accumulated
        # position is '100', which is divisible by the number of dials
        # exactly once.
        # Starting at '0' and moving 'R100' also yields position '100'.
        self.passed_zeros += new_position_sum // self.number_of_dials

        self.current_position = new_position
        self.recorded_stops.append(new_position)

    def turn_left(self, distance: int):
        new_position_sum = self.current_position - distance
        new_position = new_position_sum % self.number_of_dials


        # Scenario 1 - The starting position is '0'
        if self.current_position == 0:
            self.passed_zeros += distance // self.number_of_dials

        # Scenario 2 - The distance is larger than the starting position
        elif distance > self.current_position:
            self.passed_zeros += 1  # account for the first time passing 0

            self.passed_zeros += (distance // self.number_of_dials) - 1  # don't count initial pass twice

            # Account for the fact that we might have a remaining distance after the round trips
            # which might cause the dial to pass 0 once more
            remainder_distance_after_revelations = distance % self.number_of_dials
            if remainder_distance_after_revelations >= self.current_position:  # >= to account landing at 0
                self.passed_zeros += 1

        # Scenario 3 - The distance we travel back is equal to the current position, ending at 0
        elif distance == self.current_position:
            # We land at 0
            self.passed_zeros += 1

        self.current_position = new_position
        self.recorded_stops.append(new_position)

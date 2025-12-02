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

        self.passed_zeros += new_position_sum // self.number_of_dials

        self.current_position = new_position
        self.recorded_stops.append(new_position)

    def turn_left(self, distance: int):
        new_position_sum = self.current_position - distance
        new_position = new_position_sum % self.number_of_dials

        if self.current_position == 0:
            self.passed_zeros += distance // self.number_of_dials
        elif distance > self.current_position:
            # We pass 0 along the way
            self.passed_zeros += ((distance - self.current_position - 1) // self.number_of_dials) + 1

            if new_position == 0:
                self.passed_zeros += 1
        elif distance == self.current_position:
            # We land at 0
            self.passed_zeros += 1

        self.current_position = new_position
        self.recorded_stops.append(new_position)

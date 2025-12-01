class VaultDial:
    def __init__(self, initial_position: int = 50):
        self.current_position = initial_position
        self.start = 0
        self.end = 99
        self.number_of_dials = len(
            range(self.start, self.end + 1)  # range() is exclusive of highest
        )
        self.recorded_stops: list[int] = []

    def turn_right(self, distance: int):
        self.update_position(distance)

    def turn_left(self, distance: int):
        self.update_position(-distance)

    def update_position(self, by_amount: int):
        new_position = self.current_position + by_amount

        # Wrap around when rotating left passes 0 or
        # rotating right passes 99
        if new_position < self.start or new_position > self.end:
            new_position = new_position % self.number_of_dials

        self.current_position = new_position
        self.recorded_stops.append(new_position)


class VaultDial:
    def __init__(self, initial_position: int = 50):
        self.current_position = initial_position

    def turn_right(self, distance: int):
        self.current_position = self.current_position + distance

    def turn_left(self, distance: int):
        self.current_position = self.current_position - distance

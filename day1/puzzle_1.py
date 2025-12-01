class VaultDial:
    def __init__(self, initial_position: int = 50):
        self.current_position = initial_position

    def turn_right(self, distance: int):
        self.update_position(distance)

    def turn_left(self, distance: int):
        self.update_position(-distance)

    def update_position(self, by_amount: int):
        new_position = self.current_position + by_amount
        self.current_position = new_position

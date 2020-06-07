class Position:
    """manages all positions."""

    def __init__(self, x, y):
        self.position = x, y

    def up(self):
        """move up."""
        x, y = self.position
        new_position = (x, y - 1)
        self.check_position(new_position)

    def down(self):
        """move down."""
        x, y = self.position
        new_position = (x, y + 1)
        self.check_position(new_position)

    def right(self):
        """move right."""
        x, y = self.position
        new_position = (x + 1, y)
        self.check_position(new_position)

    def left(self):
        """move left."""
        x, y = self.position
        new_position = (x - 1, y)
        self.check_position(new_position)

    def check_position(self, new_position):
        """checks on the new position."""
        # check that this new position is indeed a path
        if new_position in self.maze_path_positions:
            # save the previous position
            self.old_position = self.position
            self.position = new_position
            # if passes over an object
            if self.position in self.items_to_collect_dict.keys():
                    # adds to inventory
                self.add_to_inventory(
                    self.items_to_collect_dict[self.position]
                )
                # if passes over the guardian
            elif self.position == self.guardian_position:
                # check if player win or loose
                self.check_if_win()

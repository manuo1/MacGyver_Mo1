from position import Position

class Guardian(Position):

    def __init__(self, x, y, is_sleeping):
        Position.__init__(self, x, y)
        self.is_sleeping = is_sleeping

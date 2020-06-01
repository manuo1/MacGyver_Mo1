from game_elements.position import Position

class Guardian(Position):

    def __init__(self, exit_position):
        x, y = exit_position
        Position.__init__(self, x, y)

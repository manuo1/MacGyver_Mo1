from game_elements.position import Position

class Guardian(Position):
    """create gardian"""
    def __init__(self, exit_position):
        x, y = exit_position
        Position.__init__(self, x, y)

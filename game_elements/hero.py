from position import Position

class Hero(Position):

    def __init__(self, x, y, inventory):
        Position.__init__(self, x, y)
        self.inventory = inventory

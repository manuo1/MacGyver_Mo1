from position import Position

class Items_To_Collect(Position):

    def __init__(self, x, y, name, is_collectable): #on ne peu pas collecter un objet 2X
        Position.__init__(self, x, y)
        self.is_collectable = is_collectable
        self.name = name

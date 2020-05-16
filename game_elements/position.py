
class Position:

    def __init__(self, x, y):
        self.position = (x, y) #crée un tuple position avec les arguments x et y

    """
    .-X->
    |
    Y
    |
    v

    """

#Déplacements

    def up(self):
        x, y = self.position
        return Position(x, y-1)

    def down(self):
        x, y = self.position
        return Position(x, y+1)

    def right(self):
        x, y = self.position
        return Position(x+1, y)

    def left(self):
        x, y = self.position
        return Position(x-1, y)

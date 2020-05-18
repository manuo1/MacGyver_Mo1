from maze_map import Maze_Map

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

#Changement de positions

    def up(self):
        x, y = self.position                            #extrait x et y du tuple position x,y = (x,y)
        new_position = (x, y-1)
        #?? test si new_position in path_positions
        self.position = new_position                    #affecte la nouvelle valeur de position


    def down(self):
        x, y = self.position
        self.position = (x, y+1)

    def right(self):
        x, y = self.position
        self.position = (x+1, y)

    def left(self):
        x, y = self.position
        self.position = (x-1, y)

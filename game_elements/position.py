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
        new_position = (x, y-1)                         #calcul la nouvelle position
        if new_position in self.path_positions:         #verifie si la nouvelle position fait bien partie des chemins
            self.position = new_position                #si oui affecte la nouvelle valeur de position

    def down(self):
        x, y = self.position
        new_position = (x, y+1)
        if new_position in self.path_positions:
            self.position = new_position

    def right(self):
        x, y = self.position
        new_position = (x+1, y)
        if new_position in self.path_positions:
            self.position = new_position

    def left(self):
        x, y = self.position
        new_position = (x-1, y)
        if new_position in self.path_positions:
            self.position = new_position
            

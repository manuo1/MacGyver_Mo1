class Position:

    def __init__(self, x, y):
        self.position = x, y


    #   .-X->
    #   |
    #   Y
    #   |
    #   v


    #Changements de positions
    def up(self):
        x, y = self.position
        new_position = (x, y-1)
        self.check_position(new_position)


    def down(self):
        x, y = self.position
        new_position = (x, y+1)
        self.check_position(new_position)


    def right(self):
        x, y = self.position
        new_position = (x+1, y)
        self.check_position(new_position)


    def left(self):
        x, y = self.position
        new_position = (x-1, y)
        self.check_position(new_position)


    #controles sur la nouvelle position
    def check_position(self,new_position):
        #verifie que cette nouvelle position est bien un chemin
        if new_position in self.maze_path_positions:
            #enregistre la position precedante
            self.old_position = self.position
            self.position = new_position
            #si passe sur un objet
            if self.position in self.items_to_collect_dict.keys():
                #demande un ajout à l'inventaire
                self.add_to_inventory(self.items_to_collect_dict[self.position])
                #si passe sur le gardien
            elif self.position == self.guardian_position:
                #controle si le joueur gagne ou perd
                self.check_if_win()

from position import Position

class Hero(Position):

    def __init__(self, x, y, path_positions, inventory): #maze.path_positions en argument pour pouvoir recuperer les position valides de deplacements
        Position.__init__(self, x, y)
        self.inventory = inventory
        self.path_positions = path_positions

    def add_to_inventory(self, name):
        self.inventory.append(name)   #ajoute le nom de l'objet collecté a l'inventaire du hero
        self.inventory.sort()         #trie l'inventaire du hero dans l'ordre alphabetique

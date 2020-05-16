from position import Position

class Maze_Map:

    def __init__(self, maze_map_filename):
        self.filename = filename
        self.floors = set() #crée un set pour les coordonées des sols
        self.walls = set()  #crée un set pour les coordonées des murs
        self.enter = set()  #crée un set pour les coordonées de l'entrée
        self.exit = set()   #crée un set pour les coordonées de la sortie

    def create_maze_map(self):

        with open(self.maze_map_filename) as infile:   #ouvre le fichier texte contenant le plan du labyrinthe et renvoi l'objet infile
            for y, line in enumerate(infile):               #pour chaque ligne du fichier recupere dans y le numero de ligne
                for x, col in enumerate(line):              #pour chaque colone de chaque lignes recupere dans x la position du caractere dans la ligne
                    if c == F:                              #si le caractere lu est un F ajoute sa position au set floor()
                        self.floors.add(Position(x, y))     #ajoute sa position au set floor()
                    elif c == W:
                        self.walss.add(Position(x, y))
                    elif c == S:
                        self.enter.add(Position(x, y))
                        self.floors.add(Position(x, y))     #l'entrée est ausssi un sol
                    elif c == X:
                        self.exit.add(Position(x, y))
                        self.floors.add(Position(x, y))     #la Sortie est ausssi un sol


class Maze_Map:


    def __init__(self, maze_map_filename):
        self.maze_map_filename = maze_map_filename
        self.path_positions = []        #crée une liste des coordonées des chemin
        #self.wall_positions = []        #crée une liste des coordonées des murs
        self.enter_positions = ()       #crée un tuple des coordonées de l'entrées
        self.exit_positions = ()       #crée un tuple des coordonées de la sorties

        with open(self.maze_map_filename) as infile:            #ouvre le fichier texte contenant le plan du labyrinthe et renvoi l'objet infile
            for y, line in enumerate(infile):                   #pour chaque ligne du fichier recupere dans y le numero de ligne
                for x, char in enumerate(line):                 #pour chaque colone de chaque lignes recupere dans x la position du caractere dans la ligne
                    if char == "P":                             #si le caractere lu est un P
                        self.path_positions.append((x, y))      #ajoute sa position à la liste path_positions[]
                    #elif char == "W":
                        #self.wall_positions.append((x, y))
                    elif char == "S":
                        self.enter_positions = (x, y)          #il n'y a qu'une entrée crée uniquement un tuple et pas une liste de tuples
                        self.path_positions.append((x, y))     #l'entrée est ausssi un chemin
                    elif char == "X":
                        self.exit_positions = (x, y)           #il n'y a qu'une sortie crée uniquement un tuple et pas une liste de tuples
                        self.path_positions.append((x, y))     #la Sortie est ausssi un chemin

    def try_postion(self,try_position):
        return try_position in path_positions:
        

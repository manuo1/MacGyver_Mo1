from random import sample

class MazeMap:


    def __init__(self, maze_map_filename):
        self.maze_map_filename = maze_map_filename
        self.path_positions = []        #liste des coordonées des chemin
        self.enter_positions = ()       #coordonées de l'entrées
        self.exit_positions = ()        #coordonées de la sorties

        with open(self.maze_map_filename) as infile:            #ouvre le fichier texte contenant le plan du labyrinthe
            for y, line in enumerate(infile):                   #pour chaque ligne de infile recupere dans y le numero de ligne
                for x, char in enumerate(line):                 #pour chaque colone de chaque lignes recupere dans x la position du caractere dans la ligne
                    if char == 'P':                             #si le caractere lu est un P
                        self.path_positions.append((x, y))      #ajoute sa position à la liste des chemins
                    elif char == 'S':
                        self.enter_positions = (x, y)
                    elif char == 'X':
                        self.exit_positions = (x, y)

        self.items_to_collects_positions = (sample(self.path_positions, 3))     #sample (du module random) renvoi une liste de 3 coordonées choisie dans path_positions
                                                                                #mais avant d'ajouter l'entree et la sortie à la liste des chemins
        self.path_positions.append(self.enter_positions)                        #Ajout l'entrée aux chemins possibles
        self.path_positions.append(self.exit_positions)                         #Ajout la sortie aux chemins possibles

        

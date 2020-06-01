import pygame
from game_elements.position import Position
from config.settings import item_to_collect_names

class Hero(Position):

    def __init__(self, enter_position, maze_path_positions, guardian_position, items_to_collect_dict): #maze.path_positions en argument pour pouvoir recuperer les position valides de deplacements
        x, y = enter_position
        Position.__init__(self, x, y)
        self.inventory = []
        self.maze_path_positions = maze_path_positions
        self.guardian_position = guardian_position
        self.items_to_collect_dict = items_to_collect_dict
        self.is_in_game = True
        self.old_position = enter_position

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_in_game = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    self.is_in_game = False
                    pygame.quit()
                elif event.key == pygame.K_RIGHT:
                    self.right()
                elif event.key == pygame.K_LEFT:
                    self.left()
                elif event.key == pygame.K_UP:
                    self.up()
                elif event.key == pygame.K_DOWN:
                    self.down()



    def add_to_inventory(self, item_to_collect_name):
        #si l'objet n'est pas deja dans l'inventaire
        if item_to_collect_name not in self.inventory:
            #ajoute le nom de l'objet collecté a l'inventaire du hero
            self.inventory.append(item_to_collect_name)
            #trie l'inventaire du hero dans l'ordre alphabetique
            self.inventory.sort()

    def check_if_win(self):
        #recupere la liste des noms des objets à collecter
        item_list = item_to_collect_names
        #trie dans l'ordre alphabetique
        item_list.sort()
        # compare les deux listes pour savoir si le joueur a collecter tout les objets
        if self.inventory == item_list:
            self.is_in_game = False
            print('WIN')
        else:
            self.is_in_game = False
            print('LOOSE')

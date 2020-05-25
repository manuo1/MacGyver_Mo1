import pygame
from settings import game_window_height, black_color

class GameWindow:

    def __init__(self):

        pygame.init()

        self.squares_size = int(game_window_height/15) #trouve une taille entiere de pixels pour divier la hauteur de l'ecran en 15

        self.height = self.squares_size*15              #recalcul la hauteur de la fentere de jeux
        self.width = int((4*self.height)/3)             #applique un format 4:3 pour calculer la largeur

        self.size = self.width, self.height

        self.surface = pygame.display.set_mode(self.size)               #crée la fenettre du jeux
        self.surface.fill(black_color)                                  #remplit la de couleur noir

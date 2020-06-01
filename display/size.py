import pygame
from config.settings import game_window_height, black_color

class Size():
    def __init__(self):

        #calcul la taille entierre d'un carré de jeu en fonction de la hauteur de fenettre choisie
        self.squares = int(game_window_height/15)
        #recalcul la hauteur de la fentere de jeux
        self.game_screen_height = self.squares*15
        #ajoute 5 cases a droite pour l'affichage du menu
        self.game_screen_width = self.squares*(15+5)
        #réaffecte la taille de l'ecran de jeu
        self.game_screen = self.game_screen_width, self.game_screen_height

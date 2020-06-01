import pygame
from config.settings import guardian_image

class GuardianDisplay(pygame.sprite.Sprite):

    def __init__ (self,squares_size, guardian_position):
        super().__init__()
        x , y = guardian_position
        #charge l'image
        self.image = pygame.image.load(guardian_image).convert_alpha()
        #redimensionne l'image à la taille d'un des carré du jeu
        self.image = pygame.transform.scale(self.image, (squares_size, squares_size))
        self.rect = self.image.get_rect()
        self.rect.x = x*squares_size
        self.rect.y = y*squares_size

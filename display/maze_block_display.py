import pygame
from config.settings import wall_image, path_image

#quand le hero passe sur l'objet il va effacer l'affichage de l'objet
class MazeBlockDisplay(pygame.sprite.Sprite):


    def __init__(self, squares_size, x, y, name):
        super().__init__() #initialise la superclasse Sprite

        if name == 'wall':
            self.image = pygame.image.load(wall_image).convert_alpha()
        elif name == 'path':
            self.image = pygame.image.load(path_image).convert_alpha()


        self.image = pygame.transform.scale(self.image, (squares_size, squares_size))
        self.rect = self.image.get_rect()
        self.rect.x = x*squares_size
        self.rect.y = y*squares_size

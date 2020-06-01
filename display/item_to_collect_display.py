import pygame
from config.settings import ether_image, needle_image, tube_image, item_to_collect_names

#quand le hero passe sur l'objet il va effacer l'affichage de l'objet
class ItemToCollectDisplay(pygame.sprite.Sprite):


    def __init__(self, squares_size, x, y, name):
        super().__init__() #initialise la superclasse Sprite

        if name == 'ether':
            self.image = pygame.image.load(ether_image).convert_alpha()
        elif name == 'needle':
            self.image = pygame.image.load(needle_image).convert_alpha()
        elif name == 'tube':
            self.image = pygame.image.load(tube_image).convert_alpha()


        self.image = pygame.transform.scale(self.image, (squares_size, squares_size))
        self.rect = self.image.get_rect()
        self.rect.x = x*squares_size
        self.rect.y = y*squares_size

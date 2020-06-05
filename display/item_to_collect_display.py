import pygame
from config.settings import (ETHER_IMAGE, NEEDLE_IMAGE, TUBE_IMAGE,
                             ITEMS_TO_COLLECT_NAMES, SQUARES_SIZE)

class ItemToCollectDisplay(pygame.sprite.Sprite):
    """creates an "item to collect" surface"""

    def __init__(self, x, y, name):
        super().__init__()
        #build image item name
        image_name = globals()[name+'_IMAGE']
        #load item image
        self.image = pygame.image.load(image_name).convert_alpha()
        #resize image
        self.image = pygame.transform.scale(self.image,
                                            (SQUARES_SIZE, SQUARES_SIZE))
        #places the surface
        self.rect = self.image.get_rect()
        self.rect.x = x*SQUARES_SIZE
        self.rect.y = y*SQUARES_SIZE

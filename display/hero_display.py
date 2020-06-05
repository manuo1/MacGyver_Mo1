import pygame
from config.settings import HERO_IMAGE, SQUARES_SIZE

class HeroDisplay(pygame.sprite.Sprite):
    """creates hero surface"""

    def __init__(self):
        super().__init__()
        #load hero image
        self.image = pygame.image.load(HERO_IMAGE).convert_alpha()
        #resize image
        self.image = pygame.transform.scale(self.image,
                                            (SQUARES_SIZE, SQUARES_SIZE))

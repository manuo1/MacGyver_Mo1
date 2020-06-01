import pygame
from config.settings import hero_image

class HeroDisplay(pygame.sprite.Sprite):
    def __init__(self, squares_size):
        super().__init__() #initialise la superclasse Sprite

        self.image = pygame.image.load(hero_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (squares_size, squares_size))

import pygame
from config.settings import PATH_IMAGE, SQUARES_SIZE, WALL_IMAGE


class MazeBlockDisplay(pygame.sprite.Sprite):
    """creates a labyrinth block surface."""

    def __init__(self, x, y, name):
        super().__init__()
        # build image block name
        image_name = globals()[name + '_IMAGE']
        # load block image
        self.image = pygame.image.load(image_name).convert_alpha()
        # resize image
        self.image = pygame.transform.scale(
            self.image, (SQUARES_SIZE, SQUARES_SIZE)
        )
        # places the block surface
        self.rect = self.image.get_rect()
        self.rect.x = x * SQUARES_SIZE
        self.rect.y = y * SQUARES_SIZE

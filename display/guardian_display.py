import pygame
from config.settings import GUARDIAN_IMAGE, SQUARES_SIZE


class GuardianDisplay(pygame.sprite.Sprite):
    """creates guerdian surface."""

    def __init__(self, guardian_position):
        super().__init__()
        x, y = guardian_position
        # load guardian image
        self.image = pygame.image.load(GUARDIAN_IMAGE).convert_alpha()
        # resize image
        self.image = pygame.transform.scale(
            self.image, (SQUARES_SIZE, SQUARES_SIZE)
        )

        # places the surface
        self.rect = self.image.get_rect()
        self.rect.x = x * SQUARES_SIZE
        self.rect.y = y * SQUARES_SIZE

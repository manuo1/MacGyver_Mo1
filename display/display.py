import pygame

class Display:

    def __init__(self, squares_size, position, image):
        pygame.init()
        self.size = (squares_size, squares_size)
        self.surface = pygame.Surface(self.size)
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)

        self.surface.blit(self.image, position)

        pygame.display.flip()

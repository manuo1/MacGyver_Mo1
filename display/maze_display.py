import pygame
from settings import white_color, path_image, wall_image
class MazeDisplay:

    def __init__(self, maze_map_filename, surface, squares_size):
        pygame.init()
        
        self.path_image = pygame.image.load(path_image)
        self.path_image = pygame.transform.scale(self.path_image, (squares_size, squares_size))     #redimensionne l'image larg,haut
        self.path_rect = self.path_image.get_rect()                                                 #crée un rectangle au deimenssion de l'image path_image

        self.wall_image = pygame.image.load(wall_image)
        self.wall_image = pygame.transform.scale(self.wall_image, (squares_size, squares_size))
        self.wall_rect = self.wall_image.get_rect()

        with open(maze_map_filename) as infile:
            for y, line in enumerate(infile):
                for x, char in enumerate(line):
                    if char == 'P' or char == 'S' or char == 'X':
                        self.path_rect.x = squares_size*x
                        self.path_rect.y = squares_size*y
                        surface.blit(self.path_image, self.path_rect)
                    elif char == 'W':
                        self.wall_rect.x = squares_size*x
                        self.wall_rect.y = squares_size*y
                        surface.blit(self.wall_image, self.wall_rect)
                        pass
        pygame.display.flip()

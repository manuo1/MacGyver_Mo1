import pygame

from config.settings import maze_map_filename, path_image
from display.hero_display import HeroDisplay
from display.guardian_display import GuardianDisplay
from display.item_to_collect_display import ItemToCollectDisplay
from display.maze_block_display import MazeBlockDisplay
#from display.menu_display import MenuDisplay

class GameDisplay:

    guardian_sprite = pygame.sprite.Group()
    items_sprites = pygame.sprite.Group()
    maze_blocks_sprites = pygame.sprite.Group()
    back_ground_menu_sprites =  pygame.sprite.Group()

    def __init__(self, squares_size, guardian_position, items_to_collect_dict):

        self.hero_display = HeroDisplay(squares_size)
        GameDisplay.guardian_sprite.add(GuardianDisplay(squares_size, guardian_position))


        #crée groupe de sprite des objets a ramasser
        for keys, values in items_to_collect_dict.items():
            x, y = keys
            name = values
            GameDisplay.items_sprites.add(ItemToCollectDisplay(squares_size, x, y, name))


        #crée groupe de sprite des blocks du labyrinthe
        with open(maze_map_filename) as infile:
            for y, line in enumerate(infile):
                for x, char in enumerate(line):
                    if char == 'P'or char == 'S' or char == 'X':
                        name = 'path'
                        GameDisplay.maze_blocks_sprites.add(MazeBlockDisplay(squares_size, x, y, name))
                    elif char == 'W':
                        name = 'wall'
                        GameDisplay.maze_blocks_sprites.add(MazeBlockDisplay(squares_size, x, y, name))

        #crée groupe de sprite des blocks en arriere plan du menu.
        for y in range(0, 16):
            for x in range(15, 20):
                GameDisplay.back_ground_menu_sprites.add(MazeBlockDisplay(squares_size, x, y, 'wall'))



        #charge une image de passage pour appliquer sur l'ancienne position du hero
        self.path_image = pygame.image.load(path_image).convert_alpha()
        self.path_image = pygame.transform.scale(self.path_image, (squares_size, squares_size))

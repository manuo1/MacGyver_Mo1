import pygame
from game_elements.maze_map import MazeMap
from game_elements.hero import Hero
from game_elements.guardian import Guardian
from game_elements.item_to_collect import ItemToCollect
from display.size import Size
from display.game_display import GameDisplay
from config.settings import path_image

#création et positionement des objets du jeu
maze = MazeMap()
guardian = Guardian(maze.exit_position)
items_to_collect = ItemToCollect(maze.items_to_collects_positions)
hero = Hero(maze.enter_position,
            maze.path_positions,
            guardian.position,
            items_to_collect.dict)
size = Size()

pygame.init()

pygame.display.set_caption("Aidez MacGyver à s'échapper !")
game_screen =pygame.display.set_mode(size.game_screen)


game_display = GameDisplay(size.squares, guardian.position, hero.items_to_collect_dict)

#applique les images qui ne seront pas rafraichies
GameDisplay.maze_blocks_sprites.draw(game_screen)
GameDisplay.items_sprites.draw(game_screen)
GameDisplay.guardian_sprite.draw(game_screen)


while hero.is_in_game:
    #appliquer l'image du menu
    GameDisplay.back_ground_menu_sprites.draw(game_screen)

    #appliquer l'image d'un chemin sur l'ancienne position pour effacer tout sur le passage du joueur
    game_screen.blit(game_display.path_image, [hero.old_position[0]*size.squares, hero.old_position[1]*size.squares])
    #applique l'image du hero
    game_screen.blit(game_display.hero_display.image, [hero.position[0]*size.squares, hero.position[1]*size.squares])
    #met à jour l'écran
    pygame.display.flip()

    hero.move()

import pygame
from game_elements.maze_map import MazeMap
from game_elements.hero import Hero
from game_elements.guardian import Guardian
from game_elements.item_to_collect import ItemToCollect
from display.game_display import GameDisplay
from config.settings import FPS


def main():
    """game main fonction"""
    #creates the maze
    maze = MazeMap()
    #creates the guardian
    guardian = Guardian(maze.exit_position)
    #creates the items to collect dictionary
    items_to_collect = ItemToCollect(maze.items_to_collects_positions)
    #creates the hero
    hero = Hero(maze.enter_position,
                maze.path_positions,
                guardian.position,
                items_to_collect.dict)

    #creates the game elements display
    game_display = GameDisplay(guardian.position, hero.items_to_collect_dict)
    #creation of the clock for setting the fps
    clock = pygame.time.Clock()
    #apply images that will not be refreshed in the game
    game_display.unrefreshed_images_blit()


    while hero.is_in_the_game:
        #apply the hero image
        game_display.hero_blit(hero.position, hero.old_position)
        #apply the hero inventory images
        game_display.hero_inventory_blit(hero.inventory)
        #check if the player move the hero
        hero.move()
        #apply end game message when player finish the game
        game_display.end_game_message(hero.win_or_loose)
        #set the game fps
        clock.tick(FPS)
        #Update the full display Surface to the game screen
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    # execute only if run as a script
    main()

import time
import pygame
from maze_display import MazeDisplay
from game_window import GameWindow
from display import Display
from settings import maze_map_filename, hero_image, guardian_image


game_window = GameWindow()
maze_display = MazeDisplay(maze_map_filename, game_window.surface, game_window.squares_size)
hero_display = Display(game_window.squares_size, (0,1), hero_image)

game_is_running = True

while game_is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False



    pygame.display.flip()

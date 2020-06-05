import os

GAME_WINDOW_HEIGHT = 800
END_TEXT_COLOR = 255, 51, 0
END_TEXT = {'win': "Vous avez gagnez !", 'loose': "Vous avez perdu !"}
FPS = 30

# create the path to the game's main directory for player's operating system
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
# list of the items to collect
ITEMS_TO_COLLECT_NAMES = ['NEEDLE', 'TUBE', 'ETHER']
# sets files paths
MAZE_MAP_TEXT_FILE = os.path.join(FILE_PATH, "maze_map_01.txt")
PATH_IMAGE = os.path.join(FILE_PATH, 'ressources', "path.png")
WALL_IMAGE = os.path.join(FILE_PATH, 'ressources', "wall.png")
HERO_IMAGE = os.path.join(FILE_PATH, 'ressources', "hero.png")
GUARDIAN_IMAGE = os.path.join(FILE_PATH, 'ressources', "guardian.png")
NEEDLE_IMAGE = os.path.join(FILE_PATH, 'ressources', "needle.png")
TUBE_IMAGE = os.path.join(FILE_PATH, 'ressources', "tube.png")
ETHER_IMAGE = os.path.join(FILE_PATH, 'ressources', "ether.png")
MENU_IMAGE = os.path.join(FILE_PATH, 'ressources', "menu_image.png")

# sets the game squares size
SQUARES_SIZE = GAME_WINDOW_HEIGHT // 15
# sets the game screen size
GAME_SCREEN_SIZE = SQUARES_SIZE * (15 + 5), SQUARES_SIZE * 15

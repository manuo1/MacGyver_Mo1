import os

game_window_height = 800

file_path = os.path.split(os.path.abspath(__file__))[0]

maze_map_filename = os.path.join(file_path, "maze_map_01.txt")
path_image = os.path.join(file_path, "path.png")
wall_image = os.path.join(file_path, "wall.png")
hero_image = os.path.join(file_path, "hero.png")
guardian_image = os.path.join(file_path, "guardian.png")
needle_image = os.path.join(file_path, "needle.png")
tube_image = os.path.join(file_path, "tube.png")
ether_image = os.path.join(file_path, "ether.png")

item_to_collect_names = ['needle','tube','ether']

black_color = 0, 0, 0
white_color = 255, 255, 255

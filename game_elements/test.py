from position import Position
from maze_map import Maze_Map
from hero import Hero
from guardian import Guardian
from items_to_collect import Items_To_Collect
import random

maze = Maze_Map("maze_map_01.txt")
hero = Hero(maze.enter_positions[0], maze.enter_positions[1], [])
guardian = Guardian(maze.exit_positions[0], maze.exit_positions[1], False)

list_of_item_to_collect = ["needle","tube","ether"]
random_position_for_items = (random.sample(maze.path_positions, 3)) #sample de random renvoi une liste de 3 coordonées choisie dans path_positions
item1 = Items_To_Collect(random_position_for_items[0][0], random_position_for_items[0][1],list_of_item_to_collect[0], True)
item2 = Items_To_Collect(random_position_for_items[1][0], random_position_for_items[1][1],list_of_item_to_collect[1], True)
item3 = Items_To_Collect(random_position_for_items[2][0], random_position_for_items[2][1],list_of_item_to_collect[2], True)

game_is_launched = True

while game_is_launched:

    print("deplacement : (z=up s=down q=left d=right) (exit pour sortir)")
    move = input()
    if move == "z":
        hero.up()
    if move == "s":
        hero.down()
    if move == "q":
        hero.left()
    if move == "d":
        hero.right()
    if move == "exit":
        game_is_launched = False


    if hero.position == item1.position and item1.is_collectable == True:
        item1.collectable = False
        hero.inventory.append(item1.name)
    elif hero.position == item2.position and item2.is_collectable == True :
        hero.inventory.append(item2.name)
        item2.is_collectable = False
    elif hero.position == item3.position and item3.is_collectable == True :
        hero.inventory.append(item3.name)
        item3.is_collectable = False

    print("position de {} : {}".format(item1.name,item1.position))
    print("position de {} : {}".format(item2.name,item2.position))
    print("position de {} : {}".format(item3.name,item3.position))
    print("position de guardian : {}".format(guardian.position))
    print("position de hero : {}, inventaire du hero :{}".format(hero.position,hero.inventory))

    if hero.position == guardian.position:
        game_is_launched = False
        print("sortie trouvée")

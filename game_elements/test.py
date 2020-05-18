from position import Position
from maze_map import Maze_Map
from hero import Hero
from guardian import Guardian
from items_to_collect import Items_To_Collect
import random

maze = Maze_Map("maze_map_01.txt")
#print(maze.path_positions)

hero = Hero(maze.enter_positions[0], maze.enter_positions[1], [])
#print ("position de hero : {}, inventaire du hero :{}".format(hero.position,hero.inventory))

guardian = Guardian(maze.exit_positions[0], maze.exit_positions[1], False)
#print ("position de guardien : {}, le gardien dort :{}".format(guardian.position,guardian.is_sleeping))

random_position_for_items = (random.sample(maze.path_positions, 3)) #sample de random renvoi une liste de 3 coordonées choisie dans path_positions

needle = Items_To_Collect(random_position_for_items[0][0], random_position_for_items[0][1], True)
#print ("position de needle : {}, on peu ramasser cet objet :{}".format(needle.position,needle.is_collectable))

tube = Items_To_Collect(random_position_for_items[1][0], random_position_for_items[1][1], True)
#print ("position de tube : {}, on peu ramasser cet objet :{}".format(tube.position,tube.is_collectable))

ether = Items_To_Collect(random_position_for_items[2][0], random_position_for_items[2][1], True)
#print ("position de ether : {}, on peu ramasser cet objet :{}".format(ether.position,ether.is_collectable))

print ("test si position du hero = position du tube : ")
hero.position = tube.position

if hero.position == needle.position and needle.is_collectable == True:
    needle.collectable = False
    hero.inventory.append("needle")
elif hero.position == tube.position and tube.is_collectable == True :
    hero.inventory.append("tube")
    tube.is_collectable = False
elif hero.position == ether.position and ether.is_collectable == True :
    hero.inventory.append("ether")
    ether.is_collectable = False

print("position de hero : {}, inventaire du hero :{}".format(hero.position,hero.inventory))
hero.up()
print("position de hero : {}, inventaire du hero :{}".format(hero.position,hero.inventory))

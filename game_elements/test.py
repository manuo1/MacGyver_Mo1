from position import Position
from maze_map import Maze_Map

coord = Position(0, 0)

print ("le type de donnée renvoyée par position :",type(coord.position))
print ("coordonées :",coord.position)
print ("->")
coord = coord.right()
print ("nouvelles coordonées :",coord.position)
print ("<-")
coord = coord.left()
print ("nouvelles coordonées :",coord.position)
print ("^")
coord = coord.up()
print ("Nouvelles coordonées :",coord.position)
print ("v")
coord = coord.down()
print ("Nouvelles coordonées :",coord.position)

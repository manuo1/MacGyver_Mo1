from random import sample
from config.settings import MAZE_MAP_TEXT_FILE

class MazeMap:
    """create the maze structure from the maze text file map"""
    def __init__(self):
        self.path_positions = []
        self.enter_position = ()
        self.exit_position = ()
        #open and use the maze map text file
        with open(MAZE_MAP_TEXT_FILE) as infile:
            #for all lines in maze map text file
            for y, line in enumerate(infile):
                #for all character in the line
                for x, char in enumerate(line):
                    #if character is P
                    if char == 'P':
                        #add position to path position list
                        self.path_positions.append((x, y))
                    #if character is S
                    elif char == 'S':
                        #set maze enter position
                        self.enter_position = (x, y)
                    #if character is X
                    elif char == 'X':
                        #set maze exit position
                        self.exit_position = (x, y)
        #add 3 random positions from the path list to the item position list
        self.items_to_collects_positions = (sample(self.path_positions, 3))
        #add enter and exit positions to path list
        self.path_positions.extend((self.enter_position, self.exit_position))

import pygame
from game_elements.position import Position
from config.settings import ITEMS_TO_COLLECT_NAMES

class Hero(Position):
    """creates hero"""
    def __init__(self, enter_position, maze_path_positions, guardian_position, items_to_collect_dict):
        x, y = enter_position
        Position.__init__(self, x, y)

        self.inventory = []
        self.maze_path_positions = maze_path_positions
        self.guardian_position = guardian_position
        self.items_to_collect_dict = items_to_collect_dict
        self.old_position = enter_position
        self.is_in_the_game = True
        self.win_or_loose = ''


    def move(self):
        """get pygame events for hero movements and quitting the game"""
        #for each event in the pygame event queue
        for event in pygame.event.get():
            #if event is exit button
            if event.type == pygame.QUIT:
                #player as left the game
                self.is_in_the_game = False
            #if event is a key pressed
            elif event.type == pygame.KEYDOWN:
                #if key pressed is escape
                if event.key == pygame.K_ESCAPE:
                    #player as left the game
                    self.is_in_the_game = False
                #if key pressed is the right arrow keys
                elif event.key == pygame.K_RIGHT:
                    #move to the right
                    self.right()
                elif event.key == pygame.K_LEFT:
                    self.left()
                elif event.key == pygame.K_UP:
                    self.up()
                elif event.key == pygame.K_DOWN:
                    self.down()



    def add_to_inventory(self, item_name):
        """add an item to inventory hero"""
        #if the item is not already in the hero's inventory.
        if item_name not in self.inventory:
            #adds the name of the collected item to the hero's inventory
            self.inventory.append(item_name)
            #sort the hero's inventory in alphabetical order
            self.inventory.sort()

    def check_if_win(self):
        """compares the hero's inventory to the list of items to collect to see if the player has collected all the items"""
        #create a copy of ITEMS_TO_COLLECT_NAMES
        item_list = ITEMS_TO_COLLECT_NAMES
        #sort the copy of the list in alphabetical order
        item_list.sort()
        #If the player has collected all the items :
        if self.inventory == item_list:
            #  the player wins
            self.win_or_loose = 'win'
        else:
            #  the player looses
            self.win_or_loose = 'loose'

from config.settings import ITEMS_TO_COLLECT_NAMES
from game_elements.position import Position


class ItemToCollect(Position):
    """create a dictionary for the items to collect."""

    # get items names
    names = ITEMS_TO_COLLECT_NAMES
    # sort list alphabetically
    names.sort()
    # create empty dictionary
    dict = {}

    def __init__(self, items_to_collects_positions):
        # for all positions in items positions list
        for positions in items_to_collects_positions:
            # get x & y from positions
            x, y = positions
            # init parent class
            Position.__init__(self, x, y)
            # get name in list
            self.name = ItemToCollect.names[
                items_to_collects_positions.index(positions)
            ]
            # add to dictionary position as key and name as value
            ItemToCollect.dict[self.position] = self.name

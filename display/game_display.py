import pygame
from config.settings import (END_TEXT, END_TEXT_COLOR, GAME_SCREEN_SIZE,
                             MAZE_MAP_TEXT_FILE, MENU_IMAGE, PATH_IMAGE,
                             SQUARES_SIZE)
from display.guardian_display import GuardianDisplay
from display.hero_display import HeroDisplay
from display.item_to_collect_display import ItemToCollectDisplay
from display.maze_block_display import MazeBlockDisplay


class GameDisplay:
    # create sprites groups
    guardian_sprite = pygame.sprite.Group()
    items_sprites = pygame.sprite.Group()
    maze_blocks_sprites = pygame.sprite.Group()
    hero_inventory_display_sprites = pygame.sprite.Group()

    def __init__(self, guardian_position, items_to_collect_dict):
        """manages all display part."""
        # initialize all imported pygame modules
        pygame.init()
        # Initialize the game screen
        self.game_screen = pygame.display.set_mode(GAME_SCREEN_SIZE)
        # Set the game screen title
        pygame.display.set_caption("Aidez MacGyver à s'échapper !")
        # create a hero display
        self.hero_display = HeroDisplay()
        # create a guardian display and add it to the guardian_sprite group
        GameDisplay.guardian_sprite.add(GuardianDisplay(guardian_position))
        # create the items to collect display and add them to the group
        self.load_items_to_collect(items_to_collect_dict)
        # create the maze blocks display and add them to the group
        self.load_maze_blocks()

        # create background menu image and a path image
        self.menu_image = pygame.image.load(MENU_IMAGE).convert_alpha()
        self.menu_image = pygame.transform.scale(
            self.menu_image, (SQUARES_SIZE * 4, SQUARES_SIZE * 11)
        )

        self.path_image = pygame.image.load(PATH_IMAGE).convert_alpha()
        self.path_image = pygame.transform.scale(
            self.path_image, (SQUARES_SIZE, SQUARES_SIZE)
        )

    def load_items_to_collect(self, items_to_collect_dict):
        """creates all items to collect."""
        # for all keys and values in the item to collect dictionary
        for keys, values in items_to_collect_dict.items():
            x, y = keys
            name = values
            # add them to items_sprites group
            GameDisplay.items_sprites.add(ItemToCollectDisplay(x, y, name))

    def load_maze_blocks(self):
        """creates all blocks of the maze."""
        # open and use the maze map text file
        with open(MAZE_MAP_TEXT_FILE) as infile:
            # for all lines in maze map text file
            for y, line in enumerate(infile):
                # for all character in the line
                for x, char in enumerate(line):
                    # if character is P or S or X
                    if char == 'P' or char == 'S' or char == 'X':
                        # add to maze_blocks_sprites group as path
                        GameDisplay.maze_blocks_sprites.add(
                            MazeBlockDisplay(x, y, 'PATH')
                        )
                    elif char == 'W':
                        # add to maze_blocks_sprites group as wall
                        GameDisplay.maze_blocks_sprites.add(
                            MazeBlockDisplay(x, y, 'WALL')
                        )
        # add more wall blocks to maze_blocks_sprites group for menu zone
        # for maze line 0 to 15
        for y in range(0, 15):
            # for maze columns from 15 to 20
            for x in range(15, 20):
                # add to maze_blocks_sprites group as wall
                GameDisplay.maze_blocks_sprites.add(
                    MazeBlockDisplay(x, y, 'WALL')
                )

    def hero_blit(self, hero_position, hero_old_position):
        """apply hero surface on the game screen and erase everything on the
        player's way."""
        # apply a path image on the game screen at the old hero position
        self.game_screen.blit(
            self.path_image,
            [
                hero_old_position[0] * SQUARES_SIZE,
                hero_old_position[1] * SQUARES_SIZE,
            ],
        )
        # apply hero image at hero position on the game screen
        self.game_screen.blit(
            self.hero_display.image,
            [hero_position[0] * SQUARES_SIZE, hero_position[1] * SQUARES_SIZE],
        )

    def unrefreshed_images_blit(self):
        """Apply on the game screen all the sprite groups that will not be
        refreshed."""
        # apply all maze blocks sprites on the game screen
        GameDisplay.maze_blocks_sprites.draw(self.game_screen)
        # apply all item to collect sprites on the game screen
        GameDisplay.items_sprites.draw(self.game_screen)
        # apply guardian sprite on the game screen
        GameDisplay.guardian_sprite.draw(self.game_screen)

    def hero_inventory_blit(self, hero_inventory):
        """Apply on the game screen hero inventory menu."""
        # clear menu display
        self.game_screen.blit(
            self.menu_image, [15 * SQUARES_SIZE, 1 * SQUARES_SIZE]
        )

        #  if hero inventory is not empty
        if hero_inventory:
            # clear hero_inventory_display_sprites group
            GameDisplay.hero_inventory_display_sprites.empty()
            # for all items in hero inventory
            for item in hero_inventory:
                # add item to hero_inventory_sprite group
                # The item will be positioned at 16 and a half squares from
                # the left of the screen and at 2 and a half squares from
                # the top of the screen + index of the hero's inventory list
                GameDisplay.hero_inventory_display_sprites.add(
                    ItemToCollectDisplay(
                        16.5, (hero_inventory.index(item) + 2.5), item
                    )
                )

            # apply hero inventory images on the game screen
            GameDisplay.hero_inventory_display_sprites.draw(self.game_screen)

    def end_game_message(self, hero_win_or_loose):
        """Apply on the game screen the end game message."""
        # if the hero end the game
        if hero_win_or_loose == 'win' or hero_win_or_loose == 'loose':
            # use os defaut font (none) with 2 maze square as size
            self.font = pygame.font.Font(None, SQUARES_SIZE * 2)
            #  draw the end text (anti-aliasing on and colored)
            self.text = self.font.render(
                END_TEXT[hero_win_or_loose], 1, END_TEXT_COLOR
            )
            #  resize text surface
            self.text = pygame.transform.scale(
                self.text, (SQUARES_SIZE * 18, SQUARES_SIZE * 3)
            )
            #  positions the text surface
            self.textpos = self.text.get_rect(
                centerx=self.game_screen.get_width() // 2,
                centery=(
                    (self.game_screen.get_height() // 2) - SQUARES_SIZE * 2
                ),
            )
            #  apply the text surface on the game screen
            self.game_screen.blit(self.text, self.textpos)

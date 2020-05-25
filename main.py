from game_elements.position import Position
from game_elements.maze_map import MazeMap
from game_elements.hero import Hero
from game_elements.guardian import Guardian
from game_elements.item_to_collect import ItemToCollect

#création et positionement de tous les objets du jeu
maze = MazeMap('maze_map_01.txt')
hero = Hero(maze.enter_positions[0], maze.enter_positions[1], maze.path_positions, [])
guardian = Guardian(maze.exit_positions[0], maze.exit_positions[1], False)
item_to_collect_1 = ItemToCollect(maze.items_to_collects_positions[0][0], maze.items_to_collects_positions[0][1], True)
item_to_collect_2 = ItemToCollect(maze.items_to_collects_positions[1][0], maze.items_to_collects_positions[1][1], True)
item_to_collect_3 = ItemToCollect(maze.items_to_collects_positions[2][0], maze.items_to_collects_positions[2][1], True)


#debut du jeux
game_is_runing = True

while game_is_runing:

    print('deplacement : (z=up s=down q=left d=right) (exit pour sortir)')
    move = input()
    if move == 'z':
        hero.up()
    if move == 's':
        hero.down()
    if move == 'q':
        hero.left()
    if move == 'd':
        hero.right()
    if move == 'exit':
        game_is_runing = False


    if hero.position == item_to_collect_1.position and item_to_collect_1.is_collectable == True:
        hero.add_to_inventory(item_to_collect_1.name)
        item_to_collect_1.is_no_longer_collectable()
    elif hero.position == item_to_collect_2.position and item_to_collect_2.is_collectable == True :
        item_to_collect_2.is_no_longer_collectable()
        hero.add_to_inventory(item_to_collect_2.name)
    elif hero.position == item_to_collect_3.position and item_to_collect_3.is_collectable == True :
        item_to_collect_3.is_no_longer_collectable()
        hero.add_to_inventory(item_to_collect_3.name)


    print('position de {} : {}'.format(item_to_collect_1.name,item_to_collect_1.position))
    print('position de {} : {}'.format(item_to_collect_2.name,item_to_collect_2.position))
    print('position de {} : {}'.format(item_to_collect_3.name,item_to_collect_3.position))
    print('position de guardian : {}'.format(guardian.position))
    print('position de hero : {}, inventaire du hero :{}'.format(hero.position,hero.inventory))


    if hero.position == guardian.position and hero.inventory == list_of_item_to_collect :
        print('WIN')
        game_is_runing = False

    elif hero.position == guardian.position and hero.inventory != list_of_item_to_collect :
        print('LOOSE')
        game_is_runing = False

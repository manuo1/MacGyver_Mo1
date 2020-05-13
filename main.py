# coding: utf-8

#import random
from random import randint
from Class_Game_Object import Game_Object
from Class_Guardian import Guardian
from Class_Hero import Hero
from Class_Item_To_Gather import Item_To_Gather


#création du Labyrinthe (object_type, pos_X, pos_Y)
maze_part_1 = Game_Object("brick",0,0)
print ("{} : Coordonées : ({}/{})".format(maze_part_1.object_type, maze_part_1.pos_X, maze_part_1.pos_Y))
maze_part_2 = Game_Object("floor",1,1)
print ("{} : Coordonées : ({}/{})".format(maze_part_2.object_type, maze_part_2.pos_X, maze_part_2.pos_Y))

#création du Héro (object_type, pos_X, pos_Y, inventory)
hero = Hero("hero",0,1,0)
print ("{} : Coordonées: {}/{}, Combien d'objet dans son inventaire : {}".format(hero.object_type, hero.pos_X, hero.pos_Y, hero.inventory))

#création du Guardien (object_type, pos_X, pos_Y, asleep)
guardian = Guardian("gardien",14,13,False)
print ("{} : Coordonées: {}/{}, Est-ce qu'il dort : {}".format(guardian.object_type, guardian.pos_X, guardian.pos_Y, guardian.asleep))

#création des objets à récuperer (object_type, pos_X, pos_Y, collectable)
item_to_gather= ["needle", "tube ", "ether"]
for item in item_to_gather:
	
	item = Item_To_Gather(item,0,0,True)
	item.pos_X = randint(1, 13) #il faudra verifier que ces coordonées sont possibles
	item.pos_Y = randint(1, 13) #il faudra verifier que ces coordonées sont possibles
	print ("{} : Coordonées: {}/{}, L'objet peut-il être ramassé : {}".format(item.object_type, item.pos_X, item.pos_Y, item.collectable))


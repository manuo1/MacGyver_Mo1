# coding: utf-8

from Class_Game_Object import Game_Object
from Class_Guardian import Guardian
from Class_Hero import Hero
from Class_Item_To_Gather import Item_To_Gather



Game_Object_1 = Game_Object("Mur",0,0)
print (Game_Object_1.appearance, Game_Object_1.pos_X, Game_Object_1.pos_Y)

Game_Object_2 = Guardian("Gardien",14,13,False)
print (Game_Object_2.appearance, Game_Object_2.pos_X, Game_Object_2.pos_Y, Game_Object_2.asleep)

Game_Object_3 = Hero("MacGyver",0,1,2)
print (Game_Object_3.appearance, Game_Object_3.pos_X, Game_Object_3.pos_Y, Game_Object_3.inventory)

Game_Object_4 = Item_To_Gather("seringue",10,6,True)
print (Game_Object_4.appearance, Game_Object_4.pos_X, Game_Object_4.pos_Y, Game_Object_4.collectable)

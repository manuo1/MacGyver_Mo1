# coding: utf-8

from Class_Game_Object import Game_Object
from Class_Guardian import Guardian
from Class_Hero import Hero
from Class_Item_To_Gather import Item_To_Gather



Game_Object_1 = Game_Object(1,1,"Mur")
print (Game_Object_1.pos_X, Game_Object_1.pos_Y, Game_Object_1.appearance)

Game_Object_2 = Guardian(1,1,"Gardien", False)
print (Game_Object_2.pos_X, Game_Object_2.pos_Y, Game_Object_2.appearance , Game_Object_2.asleep)

Game_Object_3 = Hero(1,1,"MacGyver", 2)
print (Game_Object_3.pos_X, Game_Object_3.pos_Y, Game_Object_3.appearance , Game_Object_3.inventory)

Game_Object_4 = Item_To_Gather(1,1,"seringue", True)
print (Game_Object_4.pos_X, Game_Object_4.pos_Y, Game_Object_4.appearance , Game_Object_4.collectable)

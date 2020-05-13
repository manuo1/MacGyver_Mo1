# coding: utf-8

#Herite de la class Game_Object 
from Class_Game_Object import Game_Object

class Item_To_Gather(Game_Object):
	"""
	add collectable Attributes (we cannot pick up the same object 2x)
	"""
	def __init__(self, object_type, pos_X, pos_Y, collectable):
		Game_Object.__init__(self, object_type, pos_X, pos_Y)
		self.collectable = collectable
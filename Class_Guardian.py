# coding: utf-8

#Herite de la class Game_Object 
from Class_Game_Object import Game_Object

class Guardian(Game_Object):
	"""
	add asleep Attributes (if the guardian sleeps we can go out)
	"""
	def __init__(self, object_type, pos_X, pos_Y, asleep):
		Game_Object.__init__(self, object_type, pos_X, pos_Y)
		self.asleep = asleep
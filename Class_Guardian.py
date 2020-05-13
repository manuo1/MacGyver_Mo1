# coding: utf-8

#Herite de la class Game_Object 
from Class_Game_Object import Game_Object

class Guardian(Game_Object):
	"""
	add asleep Attributes (if the guardian sleeps we can go out)
	"""
	def __init__(self, pos_X, pos_Y, appearance, asleep):
		Game_Object.__init__(self, pos_X, pos_Y, appearance)
		self.asleep = asleep
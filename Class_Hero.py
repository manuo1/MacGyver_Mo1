# coding: utf-8

#Herite de la class Game_Object 
from Class_Game_Object import Game_Object

class Hero(Game_Object):
	"""
	add invetory Attributes (we need to know if the hero 
	has all the objects to create the syringe)
	"""
	def __init__(self, pos_X, pos_Y, appearance, inventory):
		Game_Object.__init__(self, pos_X, pos_Y, appearance)
		self.inventory = inventory
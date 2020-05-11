# coding: utf-8

#Herite de la class square 
import Square

class Hero(Square):
	"""
	add invetory Attributes (we need to know if the hero 
	has all the objects to create the syringe)
	"""
	def __init__(self, pos_X, pos_Y, appearance, inventory):
		Square.__init__(pos_X, pos_Y, appearance)
		self.inventory = inventory
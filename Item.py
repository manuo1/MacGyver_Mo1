# coding: utf-8

#Herite de la class square 
import Square

class Item(Square):
	"""
	add collectable Attributes (we cannot pick up the same object 2x)
	"""
	def __init__(self, pos_X, pos_Y, appearance, collectable):
		Square.__init__(pos_X, pos_Y, appearance)
		self.collectable = collectable
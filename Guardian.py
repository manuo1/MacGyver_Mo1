# coding: utf-8

#Herite de la class square 
import Square

class Guardian(Square):
	"""
	add asleep Attributes (if the guardian sleeps we can go out)
	"""
	def __init__(self, pos_X, pos_Y, appearance, asleep):
		Square.__init__(pos_X, pos_Y, appearance)
		self.asleep = asleep
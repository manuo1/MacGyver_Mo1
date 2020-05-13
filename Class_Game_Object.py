# coding: utf-8

#Classe Mère
class Game_Object:
	"""
	All objects in the game will have a type and coordinates 
	"""
	def __init__(self, object_type, pos_X, pos_Y):
		self.object_type = object_type
		self.pos_X = pos_X
		self.pos_Y = pos_Y
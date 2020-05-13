# coding: utf-8

#Classe Mère
class Game_Object:
	"""
	All objects in the game will have an appearance and coordinates 
	"""
	def __init__(self, appearance, pos_X, pos_Y):
		self.appearance = appearance
		self.pos_X = pos_X
		self.pos_Y = pos_Y
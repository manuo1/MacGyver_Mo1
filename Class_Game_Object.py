# coding: utf-8

#Classe Mère
class Game_Object:
	"""
	All objects in the game will have coordinates and an appearance
	"""
	def __init__(self, pos_X, pos_Y, appearance):
		self.pos_X = pos_X
		self.pos_Y = pos_Y
		self.appearance = appearance
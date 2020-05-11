# coding: utf-8

#Classe Mère
class Square:
	"""
	The game will be cut into a grid of 15x15 square, 
	each box will be an object with coordinates and an appearance
	"""
	def __init__(self, pos_X, pos_Y, appearance):
		print("creation d'une boite")
		self.pos_X = pos_X
		self.pos_Y = pos_Y
		self.appearance = appearance
from Robo import Robo

class Robo3D(Robo):
	"""docstring for Robo3D"""
	def __init__(self, x, y, z):
		super(Robo3D, self).__init__(x, y)
		self.z = z

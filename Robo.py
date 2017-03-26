import random

class Point(object):
	"""docstring for Point"""
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Reward(Point):
	"""docstring for Reward"""
	def __init__(self, x, y, name):
		super(Reward, self).__init__(x, y)
		self.name = name
		

class Robo(Point):
	"""docstring for Robo"""
	def move_up(self):
		if self.y < 10:self.y += 1
		else:print('Movimento proibido') 

	def move_down(self):
		if self.y > 0:self.y -= 1
		else:print('Movimento proibido')

	def move_left(self):
		if self.x > 0:self.x -= 1
		else:print('Movimento proibido')

	def move_right(self):
		if self.x < 10:self.x += 1
		else:print('Movimento proibido')

def check_reward(robot, rewards):
	ok = False
	for reward in rewards:
		if reward.x == robot.x and reward.y == robot.y:
			print("O robô achou a recompensa: %s" %reward.name)
			ok = True
	return ok

r1 = Reward(random.randint(0,10), random.randint(0,10), 'moeda')
r2 = Reward(random.randint(0,10), random.randint(0,10), 'gasolina')
r3 = Reward(random.randint(0,10), random.randint(0,10), 'arma')
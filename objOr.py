import random
import math
class Fish(object):
	"""docstring for Fish"""
	def __init__(self, name):
		super(Fish, self).__init__()
		self.name = name
		self.price = 100

class aquarium(object):
	"""docstring for aquarium"""
	def __init__(self, name, default_fish):
		self.name = name
		self.money = 1000
		self.default_fish = default_fish
		self.fill_fishtank()

	def fill_fishtank (self):
		self.fishtank = []
		for i in range(0,math.floor(random.uniform(1,10))):
			self.fishtank.append(self.default_fish())
			self.money = self.money - self.default_fish.price

	def sell_fish(self, fish):
		if fish < len(self.fishtank):
			del self.fishtank[fish]
			self.money = self.money + 100

class sharkAquarium(aquarium):
	def __init__(self, name, default_fish, dangerlevel):
		aquarium.__init__(self, name)
		self.dangerlevel = dangerlevel
		self.money = 10000
		self.default_fish = default_fish
		self.fill_fishtank()
     
def main():
	standard_fish = Fish('trout')
	fucking_horrbile_fish = Fish('HAMMERTIME')
	fucking_horrbile_fish.price = 1000
	joes = aquarium('Joes Fish Tank', standard_fish)
	franks = aquarium('Franks Diving Bell', standard_fish)
	bills = sharkAquarium('Bills Jaws', 'VERY FUCKING HIGH', fucking_horrbile_fish)
	joes.sell_fish(1)
	bills.
	print 'Joes:', joes.__dict__
	print 'Franks:', franks.__dict__
	print 'Bills:', bills.__dict__

if __name__ == "__main__":
    main()



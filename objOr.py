import random

class aquarium(object):
	"""docstring for aquarium"""
	def __init__(self, name):
		self.name = name
		self.money = 100
		self.default_fish = "trout"
		self.fill_fishtank()

	def fill_fishtank (self):
		for i in range(0,random.random()):
			self.fishtank.append(self.default_fish())


	def sell_fish(self, fish):
		if fish < len(self.fishtank):
			del self.fishtank[fish]
			self.money = self.money + 100

class sharkAquarium(aquarium):
	def __init__(self, name, dangerlevel):
		aquarium.__init__(self, name)
		self.dangerlevel = dangerlevel
		self.default_fish = "GREAT MOTHER FUCKING WHITE"
     
def main():
	joes = aquarium('Joes Fish Tank')
	franks = aquarium('Franks Diving Bell')
	bills = sharkAquarium('Bills Jaws', 'VERY FUCKING HIGH')
	joes.sell_fish(1)
	bills.
	print 'Joes:', joes.__dict__
	print 'Franks:', franks.__dict__
	print 'Bills:', bills.__dict__

if __name__ == "__main__":
    main()



class Animal:
	def desc(self, extra : str = ""):
		print("I'm a "+extra+"animal")

class Mammal(Animal):
	def desc(self, ex : str = ""):
		super().desc(ex+"mammal: ")

class Human(Mammal):
	def desc(self):
		super().desc("human: ")

carl = Human()
carl.desc()
print(Human.__mro__)
class Human:
	def hello(self):
		return ("Hello, I'm a human")

class Citizen(Human):
	def hello(self):
		return ("Hello, I'm a citizen")

class Employee(Human):
	def hello(self):
		return ("Hello, I'm a employee")

class Renter(Citizen, Employee):
	pass

harry = Renter()
print(harry.hello())
print(Renter.__mro__)
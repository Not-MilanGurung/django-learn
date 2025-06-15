# Define a class (blueprint)
class Dog:
	# Constructor (initializer)
	def __init__(self, name, age):
		self.name = name	# Attribute
		self.age = age		# Attribute

	# Method (funciton inside class)
	def bark(self):
		print(f'{self.name} says Woof!')

# Create objects (instances)
dog1 = Dog("Mark", 10)
dog2 = Dog("Pablo", 5)

# Access attributes and methods
dog1.bark()
dog2.bark()

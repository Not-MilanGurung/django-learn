class Bird:
	def sound(self):
		return "Me bird"

class Parront(Bird):
	def sound(self):
		return super().sound() + ", Me parrot"

class Crow(Bird):
	def sound(self):
		return super().sound() + ", Me Kaw"

for bird in [Parront(), Crow()]:
	print(bird.sound())
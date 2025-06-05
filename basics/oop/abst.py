from abc import ABC, abstractmethod
from math import pi 

class Shape(ABC):
	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass

class Circle(Shape):
	def __init__(self, radius : float = 0):
		self.radius = radius

	def area(self) -> float:
		return pi * self.radius ** 2
	
	def perimeter(self) -> float:
		return 2 * pi * self.radius
	
if __name__ == '__main__':
	c = Circle(2.5)

	print("radius = "+str(c.area()))
	print("perimeter = "+str(c.perimeter()))
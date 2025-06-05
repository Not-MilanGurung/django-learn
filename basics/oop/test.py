class Shape:
	def draw(self):
		return "Drawing a shape"

class Circle(Shape):
	def draw(self):
		return "Drawing a circle"
	
class Square(Shape):
	def draw(self):
		return "Drawing a square"

class Triangle(Shape):
	def draw(self):
		return "Drawing a triangle"

	
class Rectangle(Shape):
	def draw(self):
		return "Drawing a rectangle"

shapes = [Circle(), Square(), Triangle(), Rectangle()]

for shape in shapes:
	print(shape.draw())

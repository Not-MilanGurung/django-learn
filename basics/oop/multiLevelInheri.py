class GrandParent:
	def __init__(self):
		self.HEIGHT_POTENTIAL =170
	def height(self):
		return self.HEIGHT_POTENTIAL

class Parent(GrandParent):
	def __init__(self):
		super().__init__()
		self.HEIGHT_POTENTIAL = (super().height() + 175)/2
	def height(self):
		return self.HEIGHT_POTENTIAL

class Child(Parent):
	def __init__(self):
		super().__init__()
		self.HEIGHT_POTENTIAL = (super().height() + 178)/2
	def height(self):
		return self.HEIGHT_POTENTIAL
	
ram = Child()

print(ram.height())
print(Child.__mro__)

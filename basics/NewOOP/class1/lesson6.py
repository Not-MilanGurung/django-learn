class MyClass:
	'''Parent class that defines the main behaviour'''
	def __init__(self, value):
		'''Storing the main value'''
		self.value = value
		self.__mainSecret = "This is a secret"

	def show(self):
		'''Displaying self.'''
		print(self.value)\
		
	def showSecret(self):
		print(self.__mainSecret)

class MyChildClass(MyClass):
	def __init__(self, value):
		super().__init__(value)

	def show(self):
		print("Child: ", self.value)


obj = MyChildClass(10)
obj.show()
obj.showSecret()
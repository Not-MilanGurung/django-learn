class Animal:
	def walk():
		return "Walking"
	def speak(self, sound : str):
		return "Generic animal sound: "+ sound

class Dog(Animal):
	SOUND = "Bark!"
	def speak(self):
		return super().speak(self.SOUND)

class Cat(Animal):
	SOUND = "Meow!"
	def speak(self):
		return super().speak(self.SOUND) 
	
if __name__ == "__main__":
	cat = Dog()
	dog = Cat()
	print(cat.speak())
	print(dog.speak())
	print(Animal.walk())
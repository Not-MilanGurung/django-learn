from abc import ABC, abstractmethod

class Vehicle(ABC):
	'''Simple abstract class'''
	@abstractmethod
	def start(self):
		'''Simple abstract method'''
		pass

class Car(Vehicle):
	def start(self):
		print("Car started")

car = Car()
car.start()
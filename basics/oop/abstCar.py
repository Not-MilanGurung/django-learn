from abc import ABC, abstractmethod

class Vehicle(ABC):
	@abstractmethod
	def start_engine(self):
		pass

class Car(Vehicle):
	def start_engine(self):
		print("Car engine started")

class Motorcycle(Vehicle):
	def start_engine(self):
		print("Motorcycle engine started")

if __name__ == '__main__':
	vehicles : list[Vehicle] = [Car(), Motorcycle()]
	for v in vehicles : 
		v.start_engine()
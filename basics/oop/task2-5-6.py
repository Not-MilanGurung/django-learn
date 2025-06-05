from abc import ABC, abstractmethod

class Transport(ABC):
	@abstractmethod
	def fare(self):
		pass

class Bus(Transport):
	def __init__(self, stops : int = 1):
		self.stops = stops
		self.ratePerStop = 5

	def fare(self) -> int:
		return self.ratePerStop * self.stops
	
class Taxi(Transport):
	def __init__(self, distance : float = 1.0):
		self.distance = distance
		self.rate = 10.0

	def fare(self) -> int:
		return self.distance * self.rate
	
if __name__ == '__main__':
	transports : list[Transport] = [Bus(3), Taxi(4.5)]
	for t in transports:
		print(t.fare())
from abc import ABC, abstractmethod

class Instrument(ABC):
	@abstractmethod
	def play_sound(self):
		pass

class Piano(Instrument):
	def play_sound(self):
		print("Piano is playing")

class Guitar(Instrument):
	def play_sound(self):
		print("Guitar is playing")

if __name__ == '__main__':
	instruments : list[Instrument] = [Piano(), Guitar()]

	for i in instruments:
		i.play_sound()
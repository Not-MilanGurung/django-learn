from abc import ABC, abstractmethod
from datetime import datetime

class Logger(ABC):
	@abstractmethod
	def log(self, message):
		pass

class ConsoleLogger(Logger):
	def log(self, message):
		print(f"{datetime.now()} - {message}")

class FileLogger(Logger):
	def __init__(self, filename : str):
		self.filename = filename

	def log(self, message):
		with open(self.filename, 'a') as file:
			file.write(f"{datetime.now()} - {message}")

if __name__ == '__main__':
	loggers : list[Logger] = [ConsoleLogger(), FileLogger("basics/oop/app.log")]

	for logger in loggers:
		logger.log("This is a log message")
class Device:
	def connect(self):
		return "Connected to the device"

class Test:
	def connect(self):
		return "MEor"

class Printer(Device):
	def connect(self):
		return "Connected to the printer"
	
class Scanner(Device):
	def connect(self):
		return "Connected to the scanner"

def setup_device(device : Test):
	print(device.connect())

devices : list[Device] = [Printer(), Scanner(), "Hello"]

for device in devices:
	if not issubclass(device.__class__, Device):
		print(device)
	else:
		setup_device(device)
class College:

	def __init__(self, name:str, address:str):
		self.name = name
		self.address = address
	
	def getName(self):
		'''Prints the name of the college object'''
		print(self.name)
	
	def getAddress(self):
		'''Prints the address of the college object'''
		print(self.address)
	
	def setName(self, newName : str) -> int:
		'''Sets the name of the object 
		
			Returns 1 if succesfull, else return 0'''
		try:
			self.name = newName
			return 1
		except Exception as e:
			print(e)
			return 0
	
	def setAddress(self, newAddress : str) -> int:
		try:
			self.address = newAddress
			return 1
		except Exception as e:
			print(e)
			return 0
		
if __name__ == "__main__":
	pcps = College("PCPS", "Kupondole, Lalitpur")

	pcps.getName()
	pcps.getAddress()
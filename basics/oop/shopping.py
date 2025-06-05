class Shopping:
	def __init__(self, basket : list, buyer = 'Buyer'):
		self.basket = basket
		self.buyer = buyer

	def __len__(self):
		print("Redefine length")
		count = len(self.basket)
		return count * 2
	
shoppirng = Shopping(['Shoes', 'dress'], 'Dante')
print(len(shoppirng))
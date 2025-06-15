class BankAccount:
	def __init__(self, balance):
		self.__balance = balance # Private attribute

	def deposit(self, amount):
		self.__balance += amount

	def get_balance(self):
		return self.__balance

account = BankAccount(10000)
account.deposit(5000)
print(account.get_balance())
		
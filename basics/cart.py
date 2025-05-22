from dice.dice import roll

items = {
	'milk' : 40,
	'egg' : 20,
	'sun flower' : 120
}

cart = {}

def add(item : str, coun : int):
	if item in cart.keys():
		cart[item] = cart[item] + coun
	elif item in items.keys():
		cart[item] = coun
	else:
		print("Item not in store")

def remove(item : str, num : int):
	if item in cart.keys():
		if cart[item] > num:
			cart[item] -= num
		elif cart[item] <= num:
			cart.pop(item)
	else:
		print("Item : "+item+" not found in cart")



def  view_cart():
	print("Items in the cart and their count: ")
	for item in cart.items():
		print(item)

def view_items():
	print("Items in the store and their price: ")
	for item in items.items():
		print(item)

def total() -> str:
	total = 0
	for item in cart.keys():
		total += cart[item] * items[item]
	return str(total)



def choice() -> int:
	print('''Enter your choice:
		1) Add item to cart
		2) Remove item from cart
		3) View items in cart
		4) View items in store
		5) Calculate total price
		''')
	c = int(input("Enter your choice: "))
	match c:
		case 1:
			item = input("Enter the name of the item to add: ")
			cou = int(input("Enter how many of the items to add: "))
			add(item, cou)
		case 2:
			item = input("Enter the name of the item to remove: ")
			cou = int(input("Enter how many to remove (>= than in cart to remove from the cart) : "))
			remove(item, cou)
		case 3:
			view_cart()
		case 4:
			view_items()
		case 5:
			print("The total is "+total())
		case _:
			print("Invalid choice. Exitting")
			return 1
	return 0

if __name__ == "__main__":
	q = 0
	while (q == 0):
		q = choice()
		print("\n")

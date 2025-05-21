def add(a: int, b: int):
	return a + b

def subtract(a: int, b: int):
	return a - b

def choice(x,y):
	print("\n1) For adding \n2) For subtracting\n")
	c = int(input("Enter choice: "))

	if (c == 1):
		print("The sum is "+str(add(x,y)))
	elif (c == 2):
		print("The difference is "+str(subtract(x,y)))
	else:
		print("Incorrect choice")
		choice(x,y)

if __name__ == "__main__":
	x = int(input("Enter a number: "))
	y = int(input("Enter another number: "))
	choice(x,y)





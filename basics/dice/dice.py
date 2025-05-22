import random
from basics.simple.simple import add

def roll():
	print("\nEnter 1 to roll the dice")
	x = int(input("Enter your choice: "))
	if (x == 1):
		num = random.randint(1,6)
		di = int(input("\nPredict the dice roll (1 to 6):"))
		if (di == num):
			print("You successfully predicted the roll\n")
		else:
			print("Sorry the dice rolled "+str(num))
		roll()
	else:
		print("Exiting")

if __name__ == "__main__":
	roll()
	print(add(4,2))

if __name__ == "__main__":
	f = open("fileHandling/text.txt", "rt")
	print(f.readline())
	a = [1,2,3]
	b = [1,2,3]
	a.extend(b)
	print(a)
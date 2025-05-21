def word_freq(sentence: str) -> dict:
	splited_words = sentence.split()
	words = {}
	for word in splited_words:
		word = word.replace(".","").replace(",","").replace("?","").replace("!","").lower()
		if word in words.keys():
			words[word] = words[word] + 1
		else:
			words.update({word:1})
	return words

def shortest_longest(dictinary: dict):
	words = list(dictinary.keys())
	shortest = words[0]
	longest = words[0]
	for word in words:
		if (len(word) > len(longest)):
			longest = word
		elif (len(word) < len(shortest)):
			shortest = word

	print("The longest word is : "+longest)
	print("The shortest word is : "+shortest)

def table_from_dict(dictinary: dict):
	from tabulate import tabulate
	header = ["Word", "Frequency"]
	print(tabulate(dictinary.items(), headers = header))

if __name__ == "__main__":
	sen = input("Enter the string: ")
	output = word_freq(sen)
	shortest_longest(output)
	table_from_dict(output)

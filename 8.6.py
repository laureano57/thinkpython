def find(word, letter, index):
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return -1

def count(word, letter):
	index = 0
	count = 0
	for i in range(len(word)):
		if find(word, letter, index) != -1:
			index = find(word, letter, index) + 1
			count = count + 1
	return count 


print count('paralelepipedo eneagrama anadenanthera paralaje', '*')
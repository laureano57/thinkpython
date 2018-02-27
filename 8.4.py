def find(word, letter, index):
	# index = 0
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return -1

palabra = 'la vieja de maggini'

print find(palabra, 'i', 4)
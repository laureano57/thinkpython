def count(word, letter):
	count = 0
	for l in word:
		if l == letter:
			count = count + 1
	return count


print count('paralelepipedo', 'z')

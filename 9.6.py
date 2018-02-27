fin = open('words.txt')

def is_abecedarian(word):			# esto hice yo
	n = 0
	for i in word:
		if ord(i) < n:
			return False
		n = ord(i)
	return True

def is_abecedariana(word):			# este es un ejemplo del libro, usando una funcion recursiva
	if len(word) <= 1:
		return True
	if word[0] > word[1]:
		return False
	return is_abecedarian(word[1:])

def abcd_words():					# con esto busco todas las palabras abecedarianas (de letras ordenadas alfabeticamente) de la lista words.txt
	count = 0

	for line in fin:
		line = line.strip()
		if is_abecedarian(line):
			print line
			count += 1

	print "Cantidad de palabras abecedarianas:", count



print is_abecedariana("abcdefghijjkk")


#abcd_words()

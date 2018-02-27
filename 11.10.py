def dict_words():
	"""
	Devuelve un diccionario con todas las palabras. En key y en value pone lo mismo.
	"""
	fin = open('words.txt')
	words = {}
	for line in fin:
		word = line.strip().lower()
		words[word] = word
	return words

def rotate_word(word, n):
	"""
	Rota las letras del string "n" casilleros hacia adelante.
	"""
	rot = ""
	for i in range(len(word)):

		a = ord(word[i]) + n	# a cada caracter lo convertimos a numero y le sumamos la rotacion

		if word[i] == " ":		# si es un espacio no lo rotamos, lo dejamos asi
			a = 32

		# para que las rotaciones sean solo dentro del rango a-z, sumo o resto 26 si se van de rango
		# antes controlo si son upper o lower

		if word[i].islower() == True:
			if a > 122:			
				a = a-26

			elif a < 97:
				a = a+26
			
		if word[i].isupper() == True:
			if a > 90:			
				a = a-26

			elif a < 65:
				a = a+26



		rot = rot + chr(a)		# voy concatenando el resultado en un nuevo string

	return rot

def rotate_pairs(words):
	count = 0

	for i in words:
		a = rotate_word(i, 13)
		if a in words:
			print i,
			print a
			count += 1

	print count

if __name__ == '__main__':
	words = dict_words()
	rotate_pairs(words)
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

print rotate_word("PROBANDO rotar PaLaBrAs", 13)


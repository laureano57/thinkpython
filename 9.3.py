fin = open('words.txt')

def avoids(word, chars):		# Dada una palabra word y un string de caracteres prohibidos chars, devuelve true si no encuentra ninguno de los chars en word
	for i in word:
		if i in chars:
			return False
	return True

def reader(fin):
	chars = raw_input("Ingrese los caracteres prohibidos:\n")

	for line in fin:
		if avoids(line.strip(), chars) == True:
			print line.strip()

print avoids("palanca","a")

"""
Para encontrar un juego de 5 caracteres que excluyan la menor cantidad de palabras,
deberia probar cada letra del abecedario, ver cuales son las 5 letras que menos 
palabras excluyen y juntarlas. (creo que esta mal por que las palabras que contienen
dos de las letras exluidas cuentan como una sola palabra y habria que exceptuar
ese caso)
"""

# def counter():
# 	abc = "abcdefghijklmnopqrstuvwxyz"
# 	d = {i}
# 	for i in abc:
# 		count_{i} = 0
# 		if i in fin.strip():
# 			count_{i} += 1
# 		print count_{i}






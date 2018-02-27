"""
tomar el item numero len(list)/2 y comparar la primer letra de mi palabra con la primer letra del item,
si la primer letra de mi palabra es menor que la primer letra del item, trabajar con la primer mitad, else trabajar con la 2da mitad
repetir procedimiento hasta que coincida la primera letra
cuando coincide la primera letra, si el indice actual es menor a len(word)-1 sumar 1 al indice y repetir desde el principio

NO LOGRE TERMINAR DE HACERLO ANDAR, AL FINAL EN EL LIBRO USAN EL MODULO BISECT EN LUGAR DE HACER TODO ESTE QUILOMBO
ANDA COMO EL ORTO, ENCUENTRA ALGUNAS PALABRAS DE LA PRIMER MITAD SOLAMENTE.

"""

fin = open('words.txt')
words = []
for line in fin:
	word = line.strip()
	words += [word]

# print words[:5]
# print len(words)

# def bisect(word):
# 	i = 0
# 	il = 0
# 	lista = words[:]
# 	# print lista[len(lista)/2][0]
# 	# print word[0] < lista[len(lista)/2][0]
# 	while i < (len(word)-1):
# 		if i > len(lista[il])-1:
# 			return
# 		elif word[i] < lista[len(lista)/2][i]:
# 			lista = lista[:len(lista)/2]
# 			il += len(lista)/2
# 		elif word[i] > lista[len(lista)/2][i]:
# 			lista = lista[len(lista)/2:]
# 			il += len(lista)/2
# 		elif word[i] == lista[len(lista)/2][i]:
# 			i += 1
# 			il += len(lista)/2
# 		else:
# 			print "no se encontro"
# 			return
# 	return il

def bisect(word):
	i = (len(words)-1)/2
	n = 2.0
	while word != words[i]:
		if word == words[i-1]:
			i = i-1
			break
		elif word == words[i+1]:
			i = i+1
			break
		elif word > words[i]:
			i += int((len(words)-1)/n)
		elif word < words[i]:
			i -= int((len(words)-1)/n)
		n = n*2.0
		# print i
	print words[i]
	return i

	
print bisect('deal')
# print words[55078]
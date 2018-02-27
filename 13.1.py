""" Estuve intentando con stripChars hacer una funcion que reemplace los caracteres punctuation por espacios.
	La idea era adosarla a stripWords para que reemplace todos esos caracteres por espacios previo a la creacion
	de la lista que devuelve esa funcion
"""




import string

def stripChars(s, c):
	"""	Toma un string 's' y devuelve un string sin ninguno de
		los caracteres del string 'c'
	"""
	l = list(s)
	for i in c:
		while i in l:
			l.remove(i)

	return ''.join(l)

def stripWords(txt, headersplit):
	"""	Toma un archivo txt (un libro) y un string a partir del cual
		separar el header del body, y devuelve una lista con todas las 
		palabras del libro. 
	"""
	fin = open(txt)
	chars_avoided = string.whitespace+string.punctuation

	for line in fin:
		if headersplit in line:
			break

	words = []

	for line in fin:
		l = []
		p = line.replace(string.punctuation, ' ')
		for i in p.split():
			l.append(i.lower().translate(None, string.punctuation))
		words.extend(l)

	return words

def countWords(l):
	"""	Toma una lista de palabras y devuelve una lista de tuples
		ordenada de mayor a menor, indicando las veces que aparece
		cada palabra en la lista.
	"""

	d = {}

	for i in l:
		if not i in d:
			d[i] = 1
		else:
			d[i] += 1

	count = list()

	for k, v in d.iteritems():
		count.append((v, k))

	count.sort(reverse=True)

	return count

def mostUsedWords(l, n):
	"""	Toma un histograma de palabras en forma de lista de tuples
		y muestra los 'n' primeros puestos de mayor a menor.
	"""
	for i in range(n):
		print l[i]

def notInWords(l):
	"""	Toma una lista de palabras (del libro) y devuelve una lista
		con las palabras del libro que no esten en el diccionario
	"""
	fin = open('words.txt')

	res = []
	d = {}

	for i in fin:
		d[i.strip()] = i.strip()
	
	for i in l:
		if not i in d and not i in res:
			res.append(i)

	return res


# t = countWords(stripWords('book.txt', '***'))

# mostUsedWords(t, 200)

for i in notInWords(stripWords('book.txt', '***')):
	print i


# f = open('words.txt')

def dictAnagrams():
	"""	Devuelve un diccionario de anagramas cuyos keys son strings de 
		combinaciones de caracteres posibles que forman mas de una palabra, 
		y cuyos values son una lista de palabras (strings) que se pueden formar 
		con dichos caracteres """

	# Variables
	d1 = dict()
	d2 = dict()

	# Procesos
	for word in open('words.txt'):
		w = ''.join(sorted(word.strip()))
		if not w in d1:
			d1[w] = [word.strip()]
		else:
			d1[w].append(word.strip())

	for k, v in d1.iteritems():
		if len(v) > 1:
			d2[k] = v
	
	return d2


def listChildren(s):
	""" Toma un string y devuelve una lista con todas las palabras
		que pueden formarse sacando una letra de ese string"""

	res = []
	words = open('words.txt')
	wordlist = []

	for w in words:
		wordlist.append(w.strip())


	for i in s:
		l = list(s)
		l.remove(i)
		r = ''.join(l)
		if r in wordlist:
			res.append(r)

	return res

def reduceWord(s):
	""" Chequea si una palabra es completamente reducible, en tal caso devuelve
		en una lista las palabras reducidas en orden """

	res = list()
	l = listChildren(s)
	
	res.append(s)

	if l == [] and len(s) > 0:
		return

	elif l == [] and len(s) == 0:
		return res
	
	else:
		for i in l:
			reduceWord(i)

# print reduceWord('sprites')



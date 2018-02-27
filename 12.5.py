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

def isMetathesisPair(s1, s2):
	""" Dados 2 anagramas en formato string, cuenta las permutaciones.
		Si hay una sola permutacion, devuelve True, sino False. """
	
	# Variables
	count = 0

	# Procesos
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			count += 1

	if count == 2:
		return True

	return False

def listMetathesisPairs(l):
	""" Toma una lista de strings, los compara y devuelve una lista
		de palabras metatesicas """

	# Variables
	m = []

	# Procesos
	for s in l:
		for i in range(len(l)):
			if isMetathesisPair(s, l[i]) and not [l[i], s] in m:
				m.append([s, l[i]])

	return m


def printMetathesisPairs():
	""" Imprime pares de palabras metatesicas """

	for v in dictAnagrams().values():
		l = listMetathesisPairs(v)
		if len(l) != 0:
			print l

printMetathesisPairs()
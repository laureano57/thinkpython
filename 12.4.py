
def readFile(f):
	return open(f).read()

def dictAnagrams():
	"""	Devuelve un diccionario de anagramas cuyos keys son todas las combinaciones
		de letras posibles que forman mas de una palabra, y cuyos values son
		las palabras que se pueden formar con dichos caracteres """

	# Variables
	d1 = dict()
	d2 = dict()

	# Procesos
	for word in open('words.txt'):
		w = tuple(sorted(word.strip()))
		if not w in d1:
			d1[w] = [word.strip()]
		else:
			d1[w].append(word.strip())

	for k, v in d1.iteritems():
		if len(v) > 1:
			d2[k] = v
	
	return d2

def sortedAnagrams(d):
	"""	Recibe un diccionario de anagramas e imprime en una lista 
		los anagramas correspondiente a la cantidad de anagramas
		posibles para cada palabra """
	
	d2 = dict()
	l = []

	for k, v in d.iteritems():
		if not len(v) in d2:
			d2[len(v)] = [v]
		else:
			d2[len(v)].append(v)

	for k, v in d2.iteritems():
		l.append((k, v))
		l.sort()

	for i in l:
		print i

# sortedAnagrams(dictAnagrams())

for k, v in dictAnagrams().iteritems():
	print k, v




# d = dictAnagrams()
# for k, v in d.iteritems():
# 	print v

# for k, v in d.iteritems():
# 	if len(k) == 8 and len(v) > 6:
# 		print k, v
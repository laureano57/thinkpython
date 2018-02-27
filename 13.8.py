from string import *
import random
from time import *

def sentences(text, headersplit):
	"""	Devuelve una lista con todas las oraciones de un texto en forma de listas de
		strings (lista de listas de strings).
	"""

	file = open(text)

	for line in file:
			if headersplit in line:
				break

	ret = [[]]
	sentenceCounter = 0
	count = 0
	for line in file:
		if 'End of the Project Gutenberg' in line:
			break
		words = line.split()
		if len(words) == 0:
			pass

		for word in words:
			if word[-1] == '.' or word[-2:] == '."':
				ret[sentenceCounter].append(word)
				sentenceCounter += 1
				ret.append(list())
			else:
				ret[sentenceCounter].append(word)
	
	return ret

def prefixSufixDict(lst, n=2):
	"""	Toma una lista de oraciones en forma de lista de strings (lista de listas de strings) 
		y devuelve un diccionario que mapea tuples de 'n' prefijos a listas de posibles 
		siguientes palabras. Por default trabaja con prefijos de 2 palabras.
	"""
	d = {}

	for i in lst:
		addSentenceToDict(i, d, n)

	return d

def addSentenceToDict(l, d, n):
	"""	Toma una oracion en forma de lista de strings y va agregando al diccionario
		'd' los 'n' prefijos (keys de tuples de strings) y sufijos (lista de strings).
		Si el prefijo ya existe, agrega el sufijo a la lista, sino genera el key:value 
		correspondiente.
	"""
	for i in range(len(l)):
		
		if i+n > len(l)-1:
			break

		else:
			prefix = tuple(l[i:i+n])
			suffix = l[i+n]

			if prefix in d:
				d[prefix].append(suffix)	
				
			else:
				d[prefix] = [suffix]

s = sentences('book.txt', '***')
d = prefixSufixDict(s, 2)


# count = 0
for k, v in d.iteritems():
	# count += 1
	# if count == 50:
	# 	break
	print k, v



words = open('words.txt')

wordlist = []

for i in words:
	wordlist.append(i.strip())


def histogram(s):

	d = dict()
	for i in s:
		if not i in d:
			d[i] = 1
		else:
			d[i] += 1
	return d


def isAnagram(s1, s2):
	"""Chequea si un string es anagrama del otro"""
	
	if not len(s1) == len(s2):
		return False

	h1 = histogram(s1)
	h2 = histogram(s2)

	if not h1 == h2:
		return False

	return True


def searchAnagrams(s, l):
	"""Dado un string y una lista, busca todos los anagramas y devuelve una lista"""

	a = []
	for i in l:
		if isAnagram(s, i):
			a.append(i)
	# l.remove(s)
	return a

def allAnagrams(words):
	"""Busca en una lista palabras con anagramas validos y devuelve un diccionario con todas las ocurrencias"""
	
	d = {}
	
	for s in words:
		t = tuple(sorted(s))
		l = searchAnagrams(s, words)
		if not t in d and len(l) != 0:
			d[t] = l
	return d

d = allAnagrams(wordlist)

# for k, v in d:
# 	print k, v
from time import *
from inlist import *


fin = open('words.txt')
words = []
for line in fin:
	word = line.strip()
	words += [word]


def list2dict(lst):
	output = {}	
	for i in lst:
		output[i] = ''
	return output

a = list2dict(words)

## pruebo lo que tarda in en encontrar algo en un diccionario
t1 = time()
print 'wooden' in a
t2 = time()
print 'Lo que tarda in en buscar algo en un diccionario:', t2-t1, 'segundos'

## pruebo lo que tarda in en encontrar lo mismo en una lista
t3 = time()
print 'wooden' in words
t4 = time()
print 'Lo que tarda in en buscar algo en una lista:', t4-t3, 'segundos'

## lo que tarda bisect en encontrar lo mismo en una lista
t5 = time()
print in_bisect(words, 'wooden')
t6 = time()
print 'Lo que tarda bisect en buscar algo en una lista:', t6-t5, 'segundos'
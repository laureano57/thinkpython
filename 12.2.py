from random import *

def sort_by_length(words):
 	t = [ ]
	for word in words:
		t.append((len(word), random(), word))	
	t.sort(reverse=True)						
	res = [ ]
	for length, rand, word in t:
		res.append(word)
	return res

words = ["pal","pala","palabrota","apalabrado","bralapa","palabrita","palabra","palabrata","patabrala"]

print sort_by_length(words)

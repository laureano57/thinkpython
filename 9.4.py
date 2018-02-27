fin = open('words.txt')

def uses_only(word, chars):
	
	for i in word:
		if i in chars == False:
			return False

	for i in chars:
		if i in word == False:
			return False
	
	return True



print uses_only("maramartarama", "")
fin = open('words.txt')

def three_cons(word):
	i = 0
	count = 0
	while i <= (len(word)-2):
		if count == 3:
			return True
		elif word[i] == word[i+1]:
			count += 1
			i += 2
			three_cons(word[i:])
		else:
			count = 0
			i += 1
	return False

def check_three():
	for line in fin:
		if three_cons(line) == True:
			print line.strip()

check_three()


fin = open('words.txt')


def has_no_e(word):
	for i in word:
		if i == 'e':
			return False
	return True

def reader(fin):
	no_e = 0
	total = 0
	for line in fin:
		total += 1
		if has_no_e(line.strip()) == True:
			no_e += 1
			print line.strip()
	print "Total palabras:", total
	print "Total palabras sin e:", no_e
	print "Porcentaje de palabras sin e:", (no_e * 100 / total), "%"

reader(fin)
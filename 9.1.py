fin = open('words.txt')

def reader(fin):
	for line in fin:
		if len(line.strip()) >= 20:
			print line.strip()

reader(fin)
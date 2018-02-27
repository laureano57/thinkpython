fin = open('words.txt')


def uses_all(word, chars):

	for i in chars:
		if not i in word:
			return False

	return True


def words_allchars(chars):
	count = 0

	for line in fin:
		line = line.strip()
		if uses_all(line, chars):
			print line
			count += 1

	print "Total palabras:", count


words_allchars("aeiouy")
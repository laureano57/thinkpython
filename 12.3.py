def histogram(s):
	d = dict()
	for i in s:
		if not i in d:
			d[i] = 1
		else:
			d[i] += 1
	return d

# print histogram('abarqlkjwebabababababamaaalasdjqjqjqjweoeiieieofpfpvv')

def read_file(filename):
    """Returns the contents of a file as a string."""
    return open(filename).read()

def most_frequent(s):
	d = histogram(s)
	lt = []
	for key in d:
		lt.append((d[key], key))
	lt.sort(reverse=True)
	for n, c in lt:
		print c, n

s = read_file('words.txt')

# most_frequent(s)

for i in s:
	print i

# print open('words.txt').read()

# a = open('words.txt')
# print type(a)
# s = a.read()
# print type(s)
# print s
def histogram(l):
	d = {}
	for i in l:
		if not i in d:
			d[i] = 1
		else:
			d[i] += 1
	return d

def has_duplicates(t):	# de allen downey
    """Returns True if any element appears more than once in (t),
    False otherwise."""
    s = t[:]
    s.sort()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

def has_duplicates0(l):	# Como resolvi el ejercicio original (10.8)
	for i in l:
		if l.count(i) > 1:
			return True
	return False

def has_duplicates1(l):	# Resolviendo con diccionarios
	d = histogram(l)
	for i in d:
		if d[i] > 1:
			return True
	return False

list1 = [1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd']
list2 = [1, 1, 2, 2, 'a', 'a', 'b', 'c']

print has_duplicates0(list2)
print has_duplicates1(list2)
# print list1
# print list2


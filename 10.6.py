def is_sorted(l):
	if l == sorted(l):
		return True
	else:
		return False

l = [3, 4, 5, 9, 123]
f = ['a', 'd', 'f']

print is_sorted(l)
print is_sorted(f)
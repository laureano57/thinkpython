def sumall(*args):
	s = 0
	for i in args:
		s += i
	return s

print sumall(2, 3)
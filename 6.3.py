def is_between(x, y, z):
	return (x<=y and y<=z) or (z<=y and y<=x)

print is_between(4, 8, 10)
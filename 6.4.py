def a(x, y):
	x = x + 1
	#print x
	#print y
	return x * y

def b(z):
	prod = a(z, z)
	print z, prod
	return prod

def c(x, y, z):
	total = x + y + z
	square = b(total)**2
	return square

x = 1
y = x + 1
print c(x, y+3, x+y)
#print c(x, y, y+1)
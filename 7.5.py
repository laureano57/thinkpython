from math import *

def factorial(n):
	if n == 0:
		return 1
	else:
		recurse = factorial(n-1)
		result = n * recurse
		return result

def estimate_pi():
	a0 = (2.0 * sqrt(2.0)) / 9801.0
	b0 = b0_serie(0)
	return 1.0 / (a0 * b0)

def b0_serie(n):
	a = 0
	while True:
		b0 = (factorial(4.0*n)*(1103.0 + 26390.0 * n))/(factorial(n)**4.0 * 396.0**(4.0*n))
		n = n + 1
		a = a + b0
		if b0 < 1e-15:
			return a

print estimate_pi()
print pi

# print b0_serie(0)
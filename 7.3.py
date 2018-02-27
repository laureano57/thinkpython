from math import *

def square_rt(a):
	if a == 0:
		return 0
	x = a/2.0 + 1.0			# Como valor aproximado use la mitad mas uno
	while True:
		#print x
		y = (x + a / x) / 2.0
		if y == x:
			break
		x = y
	return x

def test_sqrt(a):
	for i in range(a):
		dif_sqrt(i)

def dif_sqrt(a):
	a = float(a)
	b = square_rt(a)
	c = sqrt(a)
	d = abs(b - c)
	sp0 = ' '*(5 - len(str(a)))
	sp1 = ' '*(13 - len(str(b)))
	sp2 = ' '*(13 - len(str(c)))
	print a,
	print sp0,
	print b,
	print sp1,
	print c,
	print sp2,
	print d



test_sqrt(101)




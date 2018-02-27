from time import *

def fibonacci1(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci1(n-1) + fibonacci1(n-2)

known = {0:0, 1:1}

def fibonacci2(n):
	if n in known:
		return known[n]

	res = fibonacci2(n-1) + fibonacci2(n-2)
	known[n] = res
	return res

t0 = time()
fibonacci1(20)
t1 = time()
fibonacci2(20)
t2 = time()

print 'fibonacci1 tarda'
print t1-t0

print 'fibonacci2 tarda'
print t2-t1
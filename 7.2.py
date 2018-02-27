def square_rt(a):
	x = a/2.0 + 1.0			# Como valor aproximado use la mitad mas uno
	while True:
		print x
		y = (x + a / x) / 2.0
		if y == x:
			break
		x = y

square_rt(144)
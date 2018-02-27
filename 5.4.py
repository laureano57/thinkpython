def is_triangle(a, b, c):
	"""
	Compara la suma de dos lados con el lado restante.
	Si uno de los lados es mayor que la suma de los otros dos, no se puede armar un triangulo
	"""
	c1 = a + b >= c
	c2 = b + c >= a
	c3 = a + c >= b
	if c1 and c2 and c3:
		print "se puede armar un triangulo"
	else:
		print "no se puede armar un triangulo"

#is_triangle(4, 4, 4)


def triangle():

	a = float(raw_input("Ingrese la longitud del lado A \n"))
	b = float(raw_input("Ingrese la longitud del lado B \n"))
	c = float(raw_input("Ingrese la longitud del lado C \n"))

	a = int(a)
	b = int(b)
	c = int(c)

	is_triangle(a, b, c)


triangle()
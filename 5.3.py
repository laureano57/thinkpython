def check_int(x):
	"""
	Se fija si lo que ingresaste es integer y devuelve True o False
	"""
	y = str(type(x))
	if y == "<type 'int'>":
		return True
	else:
		return False


def check_fermat(a, b, c, n):

	fermat_1 = a**n + b**n
	fermat_2 = c**n

	if n>1 and fermat_1 == fermat_2:
		print "A la flauta! Fermat estaba en cualquiera!"
#		return True
	else:
		print "Nah, negro, eso no da ni a palos"
#		return False


def fermat():
	
	a = int(raw_input("Ingrese el primer numero \n"))
	b = int(raw_input("Ingrese el segundo numero \n"))
	c = int(raw_input("Ingrese el tercer numero \n"))
	n = int(raw_input("Ingrese el indice \n"))
	
	check_fermat(a, b, c, n)

	t1 = str(a**n)
	t2 = str(b**n)
	t3 = str(c**n)

	print t1+"+"+t2+"="+t3

fermat()


def any_lowercase1(s):
	"""
	Atraviesa el string de izquierda a derecha, 
	si encuentra en el primer lugar una mayuscula devuelve false y termina
	"""
	for c in s:
		if c.islower():
			return True
		else:
			return False

def any_lowercase2(s):
	"""
	Esta mal, da siempre true por que 'c' siempre va a ser lowercase (es un string constante)
	"""
	for c in s:
		if 'c'.islower():
			return 'True'
		else:
			return 'False'

def any_lowercase3(s):
	"""
	Esta mal, va a devolver true o false segun el ultimo caracter del string
	"""
	for c in s:
		flag = c.islower()
	return flag

def any_lowercase4(s):
	"""
	Esta ok. Inicializa flag en false e itera recorriendo el string.
	Cuando encuentra un solo lowercase, flag ya queda en True y la salida es True hasta el final.
	"""
	flag = False
	for c in s:
		flag = flag or c.islower()
	return flag

def any_lowercase5(s):
	"""
	Esta mal, tira False cada vez que la iteracion encuentra una mayuscula, y si no encuentra ninguna devuelve True.
	"""
	for c in s:
		if not c.islower():
			return False
	return True

print any_lowercase5('dqlkweqoweqouwgrlkjalksdjJ')
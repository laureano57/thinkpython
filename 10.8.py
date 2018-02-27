from random import *

def has_duplicates(t):
	if not isinstance(t, list):
		print 'El objeto debe ser de tipo lista'
		return
	for i in t:
		if t.count(i) > 1:
			return True
	return False

# list1 = [1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd']
# list2 = [1, 1, 2, 2, 'a', 'a', 'b', 'c']
# list3 = 'hola'

# print has_duplicates(list1)
# print has_duplicates(list2)
# print has_duplicates(list3)
# print list1
# print list2


def random_births(p):
	"""
	Devueve una lista de p edades aleatorias entre 0 y 100
	"""
	births = []
	for i in range(p):
		births.append(randint(1, 365))
	return births

def birth_paradox(i, p):
	"""
	Para i = iteraciones y p = cantidad de personas, calcula el porcentaje de veces que hay 2 personas con la misma edad
	"""
	parcial = 0.0
	for t in range(i):
		births = random_births(p)
		if has_duplicates(births):
			parcial += 1
	result = (parcial / i) * 100.0
	return result

print 'El porcentaje de probabilidades de que en un grupo de 23 personas haya 2 que cumplan anios el mismo dia es del',
print birth_paradox(10000, 20), '%'

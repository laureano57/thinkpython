def histogram(s):
	"""
	Devuelve un diccionario con los caracteres del string como keys y la cantidad de veces que aparece cada caracter como values
	"""
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d

def print_hist(h):
	"""
	Imprime en orden los keys de un diccionario 
	seguidos de sus respectivos valores
	"""
	l = h.keys()
	l.sort()
	for s in l:
		print s,
		print h[s]

def reverse_lookup(d, v):
	"""
	Devuelve en una lista todos los keys del diccionario 
	donde se encuentre el valor v
	"""
	l = []
	for k in d:
		if d[k] == v:
			l.append(k)
	return l

h = histogram('assdddffffggggghhhhhh')


def invert_dict(d):
	"""
	Invierte keys por values de un diccionario dado
	Los values resultantes son del tipo list
	Si hay values identicos en el diccionario inicial, al convertirlos en keys 
	devuelve como value de ese key una lista con los keys donde se encontraban 
	los values del diccionario inicial
	"""
	inverse = dict()
	for key in d:
		val = d[key]
		if not val in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse

# print invert_dict(h)

print h

def invert_dict2(d):
	inverse = dict()
	for key in d:
		val = d[key]
		inverse.setdefault(val, []).append(key)		# Si no encuentra val, lo crea y de value le carga una lista
													# a la que le aplica el metodo append y le carga el key.
													# Si lo encuentra, con append le carga a la lista el key.

	return inverse

print invert_dict2(h)
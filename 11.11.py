"""
Condiciones:
- Debe tener 5 letras
- Con esa palabra se deben formar 2 palabras reales mas sacandole la primer y la segunda letra
- Las tres palabras deben sonar igual (el value del diccionario debe ser el mismo, se puede hacer busqueda inversa)
- 
"""

def pron_dict():
	prondict = open('c06d.txt')
	d = {}
	prefixes = ('#','!','"','%','&',"'",'(',')',',','-','.','/','0',':',';','?','{','}')
	for line in prondict:
		if line.startswith(prefixes): continue
		a = line.strip().lower()
		l = a.split()
		d[l[0]] = ' '.join(l[1:])
	return d

def are_homophones(a, b, c, d):
	"""
	Chequea si a, b y c son homofonas
	"""
	if d[a] == d[b] == d[c]:
		return True
	else:
		return False

def check_words(a, b, d):
	"""
	Revisa que las palabras a y b esten en el diccionario d
	"""
	if a in d and b in d:
		return True
	else:
		return False


if __name__ == '__main__':

	d = pron_dict()

	for w0 in d:
		w1 = w0[0:1]+w0[2:]
		w2 = w0[1:]

		if check_words(w1, w2, d) and are_homophones(w0, w1, w2, d) and (len(w0) == 5):
			print w0
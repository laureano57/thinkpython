"""

"a" es el resultado de elevar un numero "b" a la n

Caso base: a = b (seria a elevado a la 1)

Si a % b == 0:
	return is_power(a/b, b)

"""

def is_power(a,b):
	if a == b:
		return True
	elif a % b == 0:
		return is_power(a/b, b)
	else:
		return False

print is_power(1024, 2)


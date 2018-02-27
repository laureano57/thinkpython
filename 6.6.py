def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1, -1]

def is_pair(word):
	if len(word) % 2 == 0:
		return True
	else:
		return False


"""
Si el numero de letras es par, las dos letras del medio deben ser iguales
Sino, la letra central es una sola.

1ero - es par o impar el numero de letras?

2do - Si es par y la longitud del string es 2 y ambas letras son iguales, 
terminar e imprimir "es palindromo", sino seguir

3ero - Si es impar y la longitud del string es 3 y la primer y ultima letra
son iguales, terminar e imprimir "es palindromo", sino seguir

4to - Si la ultima y la primera letra son distintas, terminar, sino seguir

5to - Sacarle el primer y el ultimo caracter al string y guardarlo en una 
variable para ingresarlo a la misma funcion recursivamente
"""


# def is_palindrome(word):		## Lo primero que se me ocurrio
	
# 	if word[0] != word[-1]:
# 		print "No es palindromo"
# 		return False

# 	elif is_pair(word) and (len(word) == 2) and (word[0] == word[-1]):
# 		print "Es palindromo"
# 		return True
	
# 	elif (not is_pair(word)) and (len(word) == 3) and (word[0] == word[-1]):
# 		print "Es palindromo"
# 		return True

# 	else:
# 		word2 = word[1:-1]
# 		is_palindrome(word2)


def is_palindrome(word):		## Lo de allen downey
	if len(word) <= 1:
		return True
	elif word[0] == word[-1]:
		return is_palindrome(word[1:-1])
	else:
		return False

print is_palindrome("sasasas")




"""
Si:
- Los 4 ultimos digitos de number son capicua, y
- Los 5 ultimos digitos de number+1 son capicua, y
- Los 4 digitos intermedios de number+2 son capicua, y
- Los 6 digitos de number+3 son capicua

return true
"""

def is_pal(thing):
	string = str(thing)
	return string == string[::-1]


def cartalk2():
	number = 100000
	while number < 999996:
		num0 = str(number)
		num1 = str(number+1)
		num2 = str(number+2)
		num3 = str(number+3)
		count = 0
		if is_pal(num0[2:6]):
			count += 1
		if is_pal(num1[1:6]):
			count += 1
		if is_pal(num2[1:5]):
			count += 1
		if is_pal(num3):
			count += 1
		if count == 4:
			print number
		number += 1

print cartalk2()

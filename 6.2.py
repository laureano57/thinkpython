from math import sqrt

def hipotenuse(side1, side2):
	squaresum = side1**2 + side2**2
	hipo = sqrt(squaresum)
	return hipo	


hipotenuse(3, 4)

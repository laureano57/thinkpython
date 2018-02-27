"""
Condiciones:
EdadMadre <= 120
EdadMadre - EdadHijo >= 16
EdadMadre > EdadHijo


"""


for i in range(99):
	a = int(str(i).zfill(2)[::-1])
	if (i < a) and (a - i == 18):
		print i, 
		print a
		# print a-i




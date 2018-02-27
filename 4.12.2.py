from swampy.TurtleWorld import *
from math import pi

world = TurtleWorld()
t = Turtle()
t.delay = 0.0000001			#aumenta la velocidad (en segundos)

def polyline(x, lenght, turnangle, sides):
	# Toma la instancia Turtle y se mueve hacia adelante (fd) una longitud determinada, tambien gira a la izquierda (lt) un angulo determinado
	for i in range(sides):
		fd(x, lenght)
		lt(x, turnangle)

def polygon(x, sides, lenght):
	# esta funcion prepara a la funcion polyline para dibujar un poligono de "sides" lados y "lenght" longitud por lado
	angle = 360 / sides
	polyline(x, lenght, angle, sides)

def arc(x, angle, radius):
	# arc prepara los parametros de polyline para dibujar un arco de un angulo y radio dados
	arc_lenght = 2 * pi * radius * angle / 360.0
	sides = int(arc_lenght / 3) + 1
	stepangle = float(angle) / sides
	steplenght = arc_lenght / sides 
	polyline(x, steplenght, stepangle, sides)

def circle(x, radius):
	# circle es un caso particular de arc, donde el angulo es fijo (360)
	arc(x, 360, radius)


def petalo(x, ang, rad):
	for i in range(2):
		arc(x, ang, rad)
		lt(x, 180.0-ang)
	
def flower(x, petalos, rad):
	for i in range(petalos):
		ang = 360.0/petalos
		petalo(x, ang, rad)
		lt(x, 360.0/petalos)

flower(t, 7, 120)






wait_for_user()
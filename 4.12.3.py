from swampy.TurtleWorld import *
from math import *


world = TurtleWorld()
t = Turtle()
t.delay = 0.001			#aumenta la velocidad (en segundos)

def polyline(x, lenght, turnangle, sides):
	# Toma la instancia Turtle y se mueve hacia adelante (fd) una longitud determinada, tambien gira a la izquierda (lt) un angulo determinado
	for i in range(sides):
		fd(x, lenght)
		lt(x, turnangle)

def polygon(x, sides, lenght):
	# esta funcion prepara a la funcion polyline para dibujar un poligono regular de "sides" lados y "lenght" longitud por lado
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

def triangle(x, lenght, side, alpha, beta):
	# alpha es el angulo distinto(360/lados), beta son los 2 angulos iguales 
	fd(x, lenght)
	lt(x, 180 - beta)
	fd(x, side)
	lt(x, 180 - alpha)
	fd(x, side)
	lt(x, 180 - beta)
	fd(x, lenght)

def pie(x, sides, lenght):
	# Omega es el angulo superior de la mitad de un triangulo, necesario para calcular los lados iguales del triangulo
	# La funcion sin() espera valor en radianes, hay que pasar el angulo a radianes multiplicando por pi/180

	alpha = 360.0 / sides
	omega = alpha/2.0
	beta = (180.0 - alpha) / 2
	theta = 180 - (2 * beta)
	side = lenght / sin(omega * pi / 180) / 2
	pd(x)
	rt(x, 180-beta)
	fd(x, side)
	lt(x, 180-beta)
	for i in range(sides):
		triangle(x, lenght, side, alpha, beta)
		lt(x, theta)
	fd(x, lenght)
	lt(x, 180-beta)
	fd(x, side)
	rt(x, 180-beta)
	pu(x)



pie(t, 5, 30)
fd(t, 60)
pie(t, 6, 30)
fd(t, 70)
pie(t, 7, 30)
die(t)

wait_for_user()


# para cualquier poligono regular:
# angulo interior = (lados - 2 * 180) / lados
# el angulo importante es el exterior
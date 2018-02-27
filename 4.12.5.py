from math import *
from polygon import *

world = TurtleWorld()    

t = Turtle()
t.delay = 0.00000001


# Para dibujar el espiral puedo fijar el angulo de arc en 1, para que lo vaya
# haciendo punto a punto. Tengo que variar el radio
# El rango serian la cantidad de pasos que daria (360 pasos por vuelta)

def spiral(x, turns, space):
	"""
	Dibuja un espiral arquimedeano

	x: TurtleWorld.Turtle

	turns: cantidad de vueltas del espiral (int)

	space: distancia perpendicular entre cada linea (default = 1, float)
	"""
	rango = turns * 360
	for i in range(rango):
		ang = x.get_heading() * pi / 180.0
		a = cos(ang) * ang*space
		b = sin(ang) * ang*space
		r = sqrt(pow(a, 2) + pow(b, 2))
		arc(x, r, 1)
	die(x)

spiral(t, 5, 2.8)

wait_for_user()
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.0001

pu(bob)
bk(bob, 100)
lt(bob)
fd(bob, 100)
rt(bob)
pd(bob)

def koch(t, n):
	if n < 3:
		fd(t, n)
		return
	m = n / 3
	koch(t,m)
	lt(t, 60)
	koch(t, m)
	rt(t, 120)
	koch(t, m)
	lt(t, 60)
	koch(t, m)


for i in range(3):
	koch(bob, 320)
	rt(bob, 120)

die(bob)

world.canvas.dump()

wait_for_user()
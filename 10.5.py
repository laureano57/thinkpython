def chop(lst):
	del lst[0]
	del lst[-1]
	return

g = [3, 4, 2, "marta", "miguel", 5, 0]

chop(g)

print g



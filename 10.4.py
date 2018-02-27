def middle(lst):
	ret = lst
	del ret[0]
	del ret[-1]
	return ret

g = [3, 4, 2, "marta", "miguel", 5, 0]

print middle(g)



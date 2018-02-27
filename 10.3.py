def cumulative_sum(l):
	parcial = 0
	t = []
	for i in range(len(l)):
		parcial = sum(l[:i+1])
		t.append(parcial)
	return t

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print cumulative_sum(lista)


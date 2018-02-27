
def nested_list_sum(lst):
	total = 0
	for i in range(len(lst)):
		if isinstance(lst[i], list):
			total += sum(lst[i])
		else:
			total += lst[i]
	return total
	
lista = [3, 4, 5, [3, 3, 3], 4, 5, [2, 3]]

print nested_list_sum(lista)

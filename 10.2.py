def capitalize_all(t):
	res = []
	for s in t:
		res.append(s.capitalize())
	return res

def capitalize_nested(t):
	total = []
	for i in t:
		if isinstance(t, list):
			total.append(capitalize_all(i))
		else:
			total.append(i.capitalize())
	return total

b = ['q', 'r', 't']

a = ['s', 'e', 'r', b]

print capitalize_nested(a)
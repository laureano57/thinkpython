def remove_dups(t):
	a = t[:]
	a.sort()
	i = 0
	while i < (len(a)-1):
		while a[i] == a[i+1]:
			del a[i]
		i += 1
	return a


t = [2, 4, 5, 1, 2, 3, 4, 1, 2, 3, 1, 1, 2, 6, 5, 2, 4, 3]

print remove_dups(t)
t.sort()
print t
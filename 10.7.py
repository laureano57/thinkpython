def is_anagram(f, s):
	f = list(f)
	s = list(s)
	if not len(f) == len(s):
		return False
	for i in f:
		if not i in s:
			return False
	for i in s:
		if not i in f:
			return False
	return True

string1 = 'simonfosil'
string2 = 'losinfimos'

print is_anagram(string1, string2)
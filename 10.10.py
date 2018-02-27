from time import *

def make_list1():
	a = []
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		a.append(word)
	return a

def make_list2():
	a = []
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		a = a + [word]
	return a

t0 = time()
list1 = make_list1()
t1 = time()
print list1[:10]
print "Tiempo con append:", t1-t0, "segundos\n"

t2 = time()
list2 = make_list2()
t3 = time()
print list2[:10]
print "Tiempo concatenando:", t3-t2, "segundos\n"

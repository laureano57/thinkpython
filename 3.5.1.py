def dotwice(f):
	f()
	f()

def dofour(f):
	dotwice(f)
	dotwice(f)

def printdoble(arg):
	print arg
	print arg

def printcuad(func, arg):
	printdoble(arg)
	printdoble(arg)

def printline():
	print '+ - - - -',

def printbar():
	print '|        ',

def printfila():
	dofour(printline)
	print '+'

def printbarras():
	dofour(printbar)
	print '|'

def printgrid():
	printfila()
	dofour(printbarras)
	printfila()
	dofour(printbarras)
	printfila()
	dofour(printbarras)
	printfila()
	dofour(printbarras)
	printfila()

printgrid()
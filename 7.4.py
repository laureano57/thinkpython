def eval_loop():
	while True:
		a = raw_input()
		if a == "done":
			break
		print eval(a)

eval_loop()
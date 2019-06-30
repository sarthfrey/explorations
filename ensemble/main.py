from ensemble import Model, Ensemble


@Model('e1', 'e2')
def f(x, y=3, z=4):
	return x + y + z

@Model('e1')
def g(y):
	return y**3

if __name__ == '__main__':
	e1 = Ensemble('e1')
	e2 = Ensemble('e2')
	print(e1(model='f',x=2))
	print(e1(model='g',y=3))
	print(e2(model='f',x=2))
	try:
		print(e2(model='g',y=3))
	except ValueError:
		pass
	try:
		print(e1(model='h',y=3))
	except ValueError:
		pass
	print(e1(3, model='f'))

def make_operation(oper,*args):
	if oper == '+':
		s = 0
		for i in args:
			s += i
	if oper == '-':
		s = 0
		for i in args:
			s =s-i	
	if oper == '*':
		s = 1
		for i in args:
			s *= i		
	return s
print(make_operation('+',7,7,2))
print(make_operation('-',5,5,-10,-20))
print(make_operation('*',7,6))
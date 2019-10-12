import random
a=input('''Vvedit chyslo vid 1 do 10   ''')
b=random.randint(1,10)
if int(a)==b:
	print('''Vy vgadaly, pravylna vidpovid - ''', str(a))
else:
	print('''Vy prograly, vashe chyslo  ''', str(a) , ''' ,vypadkove chyslo  ''', str(b))
a=range(1,100)
b=[]

for i in a:
	if i % 7 == 0 and not i % 5 == 0:
		b.append(i)
print(b)

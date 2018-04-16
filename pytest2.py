#!/usr/bin/python3
#recycle test
n = int(input("Enter a integer:"))
print(n,'=',end='')
i=2
while n!=1:
	while n % i ==0:
		n //=i
		if n ==1:
			print('{:d}'.format(i))
		else:
			print('{:d}*'.format(i),end = "")
	i +=1

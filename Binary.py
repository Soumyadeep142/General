import numpy as np
x=float(input('give number'))
y=np.abs(x)
z=float(y)-int(y)
a=int(y)
c=''
while a>0:
	b=a%2
	a=a//2
	c=c+str(b)
c=c[::-1]
if '.' in str(x):
	c=c+'.'
	while z>0:
		z=z*2
		c=c+str(int(z))
		z=float(z)-int(z)
if x<0:	
	c='-'+c
elif x==0:
	c=0
else:
	c='+'+c
print(c)

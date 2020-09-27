from matplotlib.pyplot import *

A='Tt'
B='Tt'
print(len(A))
def inp():
	a=[]
	b=[]
	for i,j in zip(A,B):
		a.append(i)
		b.append(j)
	a=list(set(a))
	b=list(set(b))

	finals=''
	sim=[]
	def output():
		for i in a:
			final1=''
			final1+=i
			s=0
			while s<2:
				final=final1
				final+=b[s]
				s+=1
				
				sim.append(finals+final)		
		return sim
	array=output()
	#print(array)
	outputs=[]
	for i in range(len(array)):
		s=[]
		for j in array[i]:
			s.append(j)
		if s[0].islower() and s[1].isupper():
			d=''
			s[0],s[1]=s[1],s[0]
			d=s[0]+s[1]
			outputs.append(d)
		else:
			d=''
			d=s[0]+s[1]
			outputs.append(d)
	return outputs

A=inp()
print(A)
B=list(set(A))
B.sort()
print(B)
c=[]
G=[]
for i in range(len(B)):
	count=0
	for j in range(len(A)):
		if B[i]==A[j]:
			count+=1
	c.append(count)
	G.append(B[i])
	print('{0}:{1}'.format(c[i],G[i]))
bar(G,c)
savefig('Monohybrid.png')
show()

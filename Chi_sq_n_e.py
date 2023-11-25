from numpy import *
from matplotlib.pyplot import *
from math import *

x, y=loadtxt('input.txt', usecols=(0,1), unpack='true')

x=x*10**-2

x1, y1=x,y

N_range=[]
chi_range=[]
B_range=[]
check=[2]                #give the power here
for N in check:
	chi_chart=[]
	B_chart=[]
	x_new,y_new=x,y

	A=zeros([N+1,N+1], float)
        
	for i in range(N+1):
		for j in range(N+1):
			num_points=array(x_new)**(i+j)
			A[i][j]=sum(num_points)
	#print(A ,'\n')

	C=zeros([N+1,1], float)

	for i in range(N+1):
			
		num_points_1=[(y_new[j]) for j in range(len(y_new))]
		num_points_2=[(x_new[j])**i for j in range(len(x_new))]
		num_points=[i*j for (i,j) in zip(num_points_1, num_points_2)]
		C[i][0]=sum(num_points)

	inv_A=linalg.inv(A)

	B=matmul(inv_A, C)
	print(B, '\n')

	def f(x,B):
		s=0
		for i in range(len(B)):
			s+=B[i]*x**i
		return s

	yfit=[]

	for i in x1:
		yfit1=f(i,B)
		yfit.append(yfit1)
	chi=0    
	for i in range(len(x1)):    
		chi=chi+((y1[i]-yfit[i]))**2
	
	N_range.append(N)
	B_range.append(B)
	chi_range.append(chi)

data=column_stack((N_range, chi_range))
savetxt('Chi_sq_n_e_op_check.txt', data, fmt='%s')

f = figure()
f.set_figwidth(25)
f.set_figheight(20)
suptitle(r'$\chi^2$ test without errorbars')
for n in range(len(N_range)):
	B=B_range[n]
	subplot(4,2,n+1)
	x_range=arange(0,max(x1),0.0001)
	f=[]
	for x in x_range:
		s=0
		po=check[n]
		for i in range(po+1):
			s+=B[i]*x**[i]
		f.append(s)
	plot(x_range,f)
	scatter(x1, y1)
	xlabel('x')
	ylabel('y')
	title(f'n={N_range[n]}')
savefig('Chi_sq_n_e_ckeck.png')
	

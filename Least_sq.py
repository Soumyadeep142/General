from numpy import *
from matplotlib.pyplot import *
from math import *

x, y, sig_y=loadtxt('input.txt', unpack='true')

x=x*10**-2

x1, y1, sig_y1=x,y,sig_y

N_range=[]
chi_range=[]
B_range=[]
trained_params_range=[]

for N in range(len(x1)-1):
	chi_chart=[]
	B_chart=[]
	trained_params=[]

	for count in range(100):
		x,y,sig_y=x1,y1,sig_y1
		x_new=[]
		y_new=[]
		sig_y_new=[]

		for i in range(N+1):
			r=random.randint(0,len(x))
			x_new.append(x[r])
			y_new.append(y[r])
			sig_y_new.append(sig_y[r])
			x=delete(x,r)
			y=delete(y,r)
			sig_y=delete(sig_y,r)

		A=zeros([N+1,N+1], float)

		for i in range(N+1):
			for j in range(N+1):
				num_points=array(x_new)**(i+j)
				den_points=array(sig_y_new)**2
				frac_points=[num_points[i]/den_points[i] for i in range(len(num_points))]
				A[i][j]=sum(frac_points)

		C=zeros([N+1,1], float)

		for i in range(N+1):
			
			num_points_1=[(y_new[j]) for j in range(len(y_new))]
			num_points_2=[(x_new[j])**i for j in range(len(x_new))]
			num_points=[i*j for (i,j) in zip(num_points_1, num_points_2)]
			den_points=[j**2 for j in (sig_y_new)]
			frac_points=[num_points[i]/den_points[i] for i in range(len(num_points))]
			C[i][0]=sum(frac_points)

		inv_A=linalg.inv(A)

		B=matmul(inv_A, C)

		def f(x,B):
			j=0
			s=0
			for i in range(len(B)):
				s+=B[i]*x**i
			return s

		yfit=[]

		for i in x:
			yfit1=f(i,B)
			yfit.append(yfit1)
		chi=0    
		for i in range(len(x)):    
			chi=chi+((y[i]-yfit[i])/sig_y[i])**2

		chi_chart.append(chi)
		B_chart.append(B)
		trained_params.append(x_new)
		
	min_chi=(min(chi_chart))
	pos = where(chi_chart == min_chi)[0][0]
	
	N_range.append(N)
	B_range.append(B_chart[pos])
	chi_range.append(min_chi)
	trained_params_range.append(trained_params[pos])

with open('chi_sq_op.txt', 'w') as f:
	f.write('N')
	f.write('	')
	f.write('chi_sq')
	f.write('		')
	f.write('B_val')
	f.write('				')
	f.write('Trained Parameters')
	f.write('\n')
for (i,j,k,l) in zip(N_range, B_range, chi_range, trained_params_range):
	with open('chi_sq_op.txt', 'a') as f:
		f.write(str(i))
		f.write('	')
		f.write(str(k[0]))
		f.write('		')
		f.write(str(j.T))
		f.write('				')
		f.write(str(l))
		f.write('\n')
		

min_chi_final=min(chi_range)
pos = where(chi_range == min_chi)[0][0]
print(N_range[pos])
print(chi_range[pos])
print(B_range[pos])
print(trained_params_range[pos])

x_range=arange(0,0.8,0.001)
f=[]
for x in x_range:
	s=0
	for i in range(N_range[pos]):
		s+=B[i]*x**[i]
	f.append(s)

plot(x_range,f)
errorbar(x1, y1, yerr=sig_y1, fmt='o')
show()

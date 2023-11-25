from numpy import *
from matplotlib.pyplot import *

x1, y1=loadtxt('pglab2_nov2022.dat', dtype='float', skiprows=1, max_rows=91, unpack='true')
x2, y2=loadtxt('pglab2_nov2022.dat', dtype='float', skiprows=95, unpack='true')

y=float(int(y1[0]))
N=2
y1=y1-y
sum_y1=sum(y1)
y2=[i/sum(y1) for i in y1]
y1=y2
A=zeros([N+1, N+1], float)
C=zeros([N+1, 1], float)

for i in range(N+1):
	for j in range(N+1):
		points_1=[x**(i+j) for x in x1]
		points_2=[y**2 for y in y1]
		points=[i*j for (i,j) in zip(points_1, points_2)]
		A[i][j]=sum(points)
		
for i in range(N+1):
	points_1=[log(y) for y in y1]
	points_2=[x**i for x in x1]
	points_3=[y**2 for y in y1]
	points=[i*j*k for (i,j,k) in zip(points_1, points_2, points_3)]
	C[i][0]=sum(points)

inv_A=linalg.inv(A)
B=matmul(inv_A, C)

xm=-B[1]/(2*B[2])
print('B=', B)
print('xm=', xm)

def f(x, mu, sigma):
	return (1/(sqrt(2*pi)*sigma)*exp(-(x-mu)**2./(2.*sigma**2))*sum_y1)+y
	
sigma=sqrt(-1/(2*B[2]))
mu=-B[1]/(2*B[2])
print('mu=', mu, 'sigma=', sigma)

x_range=arange(min(x1), max(x1), 0.1)
fx_range=[]
for x in x_range:
	fx_range.append(f(x, mu, sigma))
plot(x_range, fx_range)
y1=[i*sum_y1+y for i in y1]
scatter(x1, y1, s=5, color='red')
title('Guo Method')
xlabel('x')
ylabel('f(x)')
savefig('Guo.png')
show()


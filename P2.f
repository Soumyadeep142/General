c P2
      implicit double precision(a-h, o-z)
      parameter(n=4, tolerance=0.0001)
      dimension a(n,n+1), x(n), temp(n,n+1)
      open(2, file='P2_Input.txt')
      open(3, file='P2_Output.txt', access='append')
      
      
c Augmented Matrix
      do 19 i=1,n
      	read(2,*)(a(i,j),j=1,n+1)
 19   continue
      write(*,*)"The Augmented Matrix is"
      do 13 k=1,n
      write(*,*) (a(k, l), l=1,n+1)
 13   continue
      write(*,*)''
      
      
c Gauss Elimination
      do 21 i=1,n-1
      	if (abs(a(i,i)).le.tolerance) then
      		write(*,*) 'It is a Pivotal Condition, Changing its order'
      		do 29 j =1,n+1
      			temp(i,j)=a(i,j)
      			a(i,j)=a(i+1,j)
      			a(i+1,j)=temp(i,j)
29		continue
      	endif
      	do 39 j=i+1,n
      		ratio=a(j,i)/a(i,i)
      		do 23 k=1,n+1
      			a(j,k)=a(j,k)-ratio*a(i,k)
 23		continue
 39	continue
 21   continue

c Back Substitution
      x(n)=a(n,n+1)/a(n, n)
      
      do 1 i=n-1,1,-1
      	x(i)=a(i,n+1)
      	do 12 j=i+1,n
      		x(i)=x(i)-a(i,j)*x(j)
 12      continue
        x(i)=x(i)/a(i,i)
 1    continue
        write(*,*)'The roots are'
        write(*,*)x 
 24   stop
      end
      


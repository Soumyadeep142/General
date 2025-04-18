c P3
      implicit double precision(a-h, o-z)
      open(2, file="P3_output.txt")
c Initialisation
      x0=0.d0
      y0=0.d0
      z0=0.d0
      write(*,*)"Precision="
      read(*,*) error
c Gauss Seidel iteration
      do 1 i=1,9999

      	x1=f(x0, y0, z0)
	y1=g(x1, y0, z0)
	z1=h(x1, y1, z0)
		      	
	e1=abs(x0-x1)
	e2=abs(y0-y1)
	e3=abs(z0-z1)
		      	
	x0=x1
	y0=y1
	z0=z1
			
	e=min(e1, e2, e3)
	if (e.lt.error) goto 39
 1    continue
 39   write(*,*) 'The solutions are'
      write(*,*)x0, y0, z0
      write(*,*)"No. of iteration"
      write(*,*)i
      write(*,*)'when precision is'
      write(*,*)error
      stop
      end
c defining functons      
      double precision function f(x,y,z)
      implicit double precision(a-h, o-z)
      f=(9+y)/5
      return
      end
      
      double precision function g(x,y,z)
      implicit double precision(a-h, o-z)
      g=(4+z+x)/5
      return
      end
      
      double precision function h(x,y,z)
      implicit double precision(a-h, o-z)
      h=(-6+y)/5
      return
      end

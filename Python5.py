import numpy as np
import matplotlib.pylab as plt
n=np.linspace(0,199,200)    
         
def x(n): 
    e=eval(f)  
    return e 

f=(input("Input Equation x(n):"))   
 
for i in range(0,200):
    if i==0:
        y=(-1.5*x(n))+(2*x(n+1))-(0.5*x(n+2))
        
    elif i > 0 & i <= 198:
        y= (0.5*x(n+1))-(0.5*x(n-1))
    
    else:
        y=(1.5*x(n))-(2*x(n-1))+(0.5*x(n-2))
        

plt.plot(x(n),color="r",label = "Line of x(n)")
plt.plot(y,color="g",label = "Line of y(n)")
plt.grid()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show

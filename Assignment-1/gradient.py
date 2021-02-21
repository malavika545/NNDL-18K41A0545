from sympy import *
import sympy as sym
x=sym.Symbol('x')
y=sym.diff(x**4+3*x**2+10)
f = lambda x1: x1**4+3*x1**2+10

print("The gradient/slope/first order derivative of given function is : ",y)

x_is=1
n=0.1
epoches=30
i=1
while(i<=epoches):
    x = y.subs(x,x_is) 
    cx=-n*(x_is)
    x_is=x_is+cx
    i=i+1
    if(i>epoches):
        break
    
print("The global minimum point of given function is at x =", round(x_is))
print("The value of the function at minimum point is {}".format(round(f(x_is))))

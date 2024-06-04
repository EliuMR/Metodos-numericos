#regla de Simpson para integración numérica en dos dimensiones. 
import sympy
import numpy as np
def simpson(f,a,b,m):
    h=(b-a)/float(m)
    s=0
    x=a
    for i in range (1,m):
        s=s+2*(i%2+1)*f(x+i*h)
    s=h/3*(f(a)+s+f(b))
    return s
def simpson3lv(f,ax,bx,h,q,mx,my):
    s=sympy.Symbol('y')
    dx=(bx-ax)/float(mx)
    v=ax
    r=[]
    for i in range(0,mx+1):
        def g(y):
            return f(v,y)
        w1=h(v)
        w2=q(v)
        #print ('i,w1,w1',i,w1,w2)
        u=simpson(g,w1,w2,my)
        r=r+[u]
        v=v+dx
    s=0
    for i in range(1,mx):
        s=s+2*(2-(i+1)%2)*r[i]
    s=dx/3.0*(r[0]+s+r[mx])
    return s
       
#La función edodif resuelve un sistema de ecuaciones diferenciales ordinarias (EDOs) de segundo orden utilizando el método de las diferencias finitas y el algoritmo de eliminación gaussiana en una matriz tridiagonal. 
from tridiagonal import tridiagonal
def edodif(P,Q,R,S,x0,y0,xn,yn,n):
    h=(xn-x0)/n
    u=[]
    a=[]
    b=[]
    c=[]
    d=[]
    for i in range(0,n-1):
        x=x0+h*i
        #Diagonales del sistema tridiagonal
        a=a+[P(x,h)]
        b=b+[Q(x,h)]
        c=c+[R(x,h)]
        d=d+[S(x,h)]
        u=u+[x]
    #Corrección para la primera ecuación
    d[0]=d[0]-a[0]*y0
    #Corrección para la última ecuación
    d[n-2]=d[n-2]-c[n-2]*yn
    v=tridiagonal(a,b,c,d)
    return[u,v]
#Esta función edodifdi resuelve un sistema de ecuaciones diferenciales ordinarias (EDOs) de primer orden, donde la condición inicial está dada por la primera derivada
from tridiagonal import tridiagonal
def edodifdi(P,Q,R,S,x0,dy0,xn,yn,n):
    h=(xn-x0)/n
    u=[]
    a=[]
    b=[]
    c=[]
    d=[]
    for i in range(0,n):
        x=x0+h*i
        #Diagonales del sistema tridiagonal
        a=a+[P(x,h)]
        b=b+[Q(x,h)]
        c=c+[R(x,h)]
        d=d+[S(x,h)]
        u=u+[x]
    x=h
    #Corrección para la primera ecuación
    c[0]=P(x,h)+R(x,h)
    d[0]=S(x,h)+P(x,h)*2*h*dy0
    #Corrección para la última ecuación
    d[n-1]=d[n-1]-c[n-1]*yn
    v=tridiagonal(a,b,c,d)
    return[u,v]
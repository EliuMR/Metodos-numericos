#implementa el método del trapecio para calcular la integral definida de una función en el intervalo [a,b]. 
def trapecio(f,a,b,m):
    h=(b-a)/float(m)
    s=0.0
    for i in range (1,m):
        s=s+f(a+i*h)
    r=h/2.0*(f(a)+2*s+f(b))
    return r
# Implementación de la regla de Simpson compuesta para aproximar la integral de una función
# f: función a integrar
# a, b: límites de integración
# m: número de subintervalos

def simpson(f,a,b,m):
    h=(b-a)/float(m)
    s=0
    x=a
    for i in range (1,m):
        s=s+2*(i%2+1)*f(x+i*h)
    s=h/3*(f(a)+s+f(b))
    return s
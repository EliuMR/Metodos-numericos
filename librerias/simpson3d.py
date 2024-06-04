# Función para aproximar la integral de una función de dos variables sobre un rectángulo usando la regla de Simpson compuesta
# f: función a integrar
# ax, bx: límites de integración en la dirección x
# ay, by: límites de integración en la dirección y
# mx, my: número de subintervalos en las direcciones x e y


import sympy
def simpson(f,a,b,m):
    h=(b-a)/float(m)
    s=0
    x=a
    for i in range (1,m):
        s=s+2*(i%2+1)*f(x+i*h)
    s=h/3*(f(a)+s+f(b))
    return s
def simpson3d(f,ax,bx,ay,by,mx,my):
    x=sympy.Symbol('x')
    dy=(by-ay)/float(my)
    v=ay
    r=[]
    for i in range (0,my+1):
        def g(x):
            return f(x,v)
        u=simpson(g,ax,bx,mx)
        r=r+[u]
        v=v+dy
    s=0
    for i in range(1,my):
        s=s+2*(2-(i+1)%2)*r[i]
    s=dy/3.0*(r[0]+s+r[my])
    
    return s
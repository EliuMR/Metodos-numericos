"""
    Implementa el método de Heun para resolver un sistema de EDOs de primer orden.

    Args:
        f: Función que define la primera ecuación diferencial.
        g: Función que define la segunda ecuación diferencial.
        x: Valor inicial de x.
        y: Valor inicial de y.
        z: Valor inicial de z.
        h: Tamaño del paso.
        m: Número de iteraciones.

    Returns:
        Tupla con tres listas, u, v y w, que contienen las coordenadas x, y, y z de los puntos de la solución.
    """

#x,y punto inicial
#Iteraciones
def heun2(f,g,x,y,z,h,m):
    u=[]
    v=[]
    w=[]
    for i in range(m):
        k1y=h*f(x,y,z)
        k1z=h*g(x,y,z)
        k2y=h*f(x+h,y+k1y,z+k1z)
        k2z=h*g(x+h,y+k1y,z+k1z)
        y=y+0.5*(k1y+k2y)
        z=z+0.5*(k1z+k2z)
        x=x+h
        u=u+[x]
        v=v+[y]
        w=w+[z]
    return [u,v,w]
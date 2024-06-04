 """
    Implementa el método de Heun para resolver una EDO de primer orden.

    Args:
        f: Función que define la ecuación diferencial.
        x: Valor inicial de x.
        y: Valor inicial de y.
        h: Tamaño del paso.
        m: Número de iteraciones.

    Returns:
        Tupla con dos listas, u y v, que contienen las coordenadas x e y de los puntos de la solución.
    """

#x,y punto inicial
#Iteraciones
def heun(f,x,y,h,m):
    u=[]
    v=[]
    for i in range(m):
        k1=h*f(x,y)
        k2=h*f(x+h,y+k1)
        y=y+0.5*(k1+k2)
        x=x+h
        u=u+[x]
        v=v+[y]
    return [u,v]
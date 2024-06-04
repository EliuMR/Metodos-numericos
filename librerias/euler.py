#Este código implementa el método de Euler para resolver una ecuación diferencial ordinaria (EDO) de primer orden de la forma \( y' = f(x, y) \). Aquí hay una descripción de la función `euler`:

#- `f`: Es la función que define la ecuación diferencial \( y' = f(x, y) \).
#- `x`, `y`: Son las condiciones iniciales, es decir, el punto inicial en el plano \( (x, y) \).
#- `h`: Es el tamaño del paso, que determina la distancia entre los puntos sucesivos en el dominio \( x \).
#- `m`: Es el número de iteraciones o pasos que el método de Euler realizará.

#El método de Euler aproxima la solución de la ecuación diferencial avanzando paso a paso desde el punto inicial \( (x, y) \) hacia adelante a lo largo del dominio \( x \). En cada paso, calcula la pendiente de la función en el punto actual \( (x, y) \) usando la función \( f(x, y) \), y luego avanza \( h \) unidades en la dirección de esa pendiente para encontrar el siguiente punto \( (x+h, y+h \cdot f(x, y)) \). Este proceso se repite \( m \) veces.

#La función `euler` devuelve dos listas, `u` y `v`, que contienen las coordenadas \( x \) e \( y \), respectivamente, de los puntos a lo largo de la solución aproximada de la ecuación diferencial.

#x,y punto inicial
#Iteraciones
def euler(f,x,y,h,m):
    u=[]
    v=[]
    for i in range(m):
        y=y+h*f(x,y)
        x=x+h
        u=u+[x]
        v=v+[y]
    return [u,v]
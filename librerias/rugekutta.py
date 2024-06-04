# Definición de la función Runge-Kutta de cuarto orden para resolver una EDO
# f: función que representa la EDO (dy/dx = f(x, y))
# x, y: punto inicial (x0, y0)
# h: tamaño del paso
# m: número de iteraciones

#x,y punto inicial
#Iteraciones
def rugekutta(f,x,y,h,m):
    u=[]
    v=[]
    for i in range(m):
        k1=h*f(x,y)
        k2=h*f(x+h/2.0,y+k1/2.0)
        k3=h*f(x+h/2.0,y+k2/2.0)
        k4=h*f(x+h,y+k3)
        y=y+1.0*1/6*(k1+2*k2+2*k3+k4)
        x=x+h
        u=u+[x]
        v=v+[y]
    return [u,v]
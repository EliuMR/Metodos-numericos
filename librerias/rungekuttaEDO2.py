#método de Runge-Kutta de cuarto orden para resolver un sistema de ecuaciones diferenciales ordinarias de segundo orden. 
# x, y: punto inicial
# Iteraciones
# f, g: funciones que definen el sistema de ecuaciones diferenciales
# h: tamaño del paso
# m: número de iteraciones

#x,y punto inicial
#Iteraciones
def rungekuttaEDO2(f,g,x,y,z,h,m):
    u=[]
    v=[]
    w=[]
    for i in range(m):
        k1y=h*f(x,y,z)
        k1z=h*g(x,y,z)
        k2y=h*f(x+h/2.0,y+k1y/2.0,z+k1z/2.0)
        k2z=h*g(x+h/2.0,y+k1y/2.0,z+k1z/2.0)
        k3y=h*f(x+h/2.0,y+k2y/2.0,z+k2z/2.0)
        k3z=h*g(x+h/2.0,y+k2y/2.0,z+k2z/2.0)
        k4y=h*f(x+h,y+k3y,z+k3z)
        k4z=h*g(x+h,y+k3y,z+k3z)
        y=y+1.0*1/6*(k1y+2*k2y+2*k3y+k4y)
        z=z+1.0*1/6*(k1z+2*k2z+2*k3z+k4z)
        x=x+h
        u=u+[x]
        v=v+[y]
        w=w+[z]
    return [u,v,w]
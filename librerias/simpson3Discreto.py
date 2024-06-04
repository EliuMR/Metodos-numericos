# Función para aproximar la integral de una función de dos variables sobre un rectángulo discretizado usando la regla de Simpson
# f: matriz de valores de la función discretizada
# ax, bx: límites de integración en la dirección x
# ay, by: límites de integración en la dirección y
# mx, my: número de divisiones en las direcciones x e y
import numpy as np
def simpson3Discreto(f,ax,bx,ay,by,mx,my):
    hx=(bx-ax)/(mx)
    hy=(by-ay)/(my)
    r=np.zeros(my+1)
    for i in range(0,my+1):
        for j in range(1,mx):
            #print(2*(j%2+1))
            r[j]=r[j]+2*(j%2+1)*f[j,i]
        r[i]=hy/3.0*(f[0,i]+r[i]+f[mx,i])
        #print(i,f[0,i],f[mx,i])
    s=0
    #print(hy,hx)
    for i in range(1,my):
        #print(2*(2-(i+1)%2))
        s=s+2*(2-(i+1)%2)*r[i]
    s=hx/3.0*(r[0]+s+r[my])
    return s
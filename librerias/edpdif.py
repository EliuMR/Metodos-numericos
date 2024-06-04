#Metodo explícito de diferencias finitas para una EDP parabólica
#U(i,j+1)=(P)U(i-1,j)+(Q)U(i,j)+RU(i+1,j)

#Este script parece implementar un método numérico para resolver una ecuación de difusión unidimensional. Aquí hay una descripción de lo que hace:

#1. Se define la función `edpdif` que calcula la distribución de temperatura en un material en función de una condición inicial `U`, y los coeficientes `P`, `Q` y `R`, que representan la difusividad, la termoconductividad y la fuente de calor, respectivamente. El parámetro `m` especifica el número de puntos espaciales en el material.

#2. Se inicializan las condiciones y los parámetros del problema, como la temperatura en los bordes (`Ta` y `Tb`), la temperatura inicial (`To`), el tamaño del paso espacial (`dx`) y temporal (`dt`), la longitud del material (`L`), la conductividad térmica (`k`) y la matriz de temperatura `U`.

#3. Se define el parámetro de estabilidad `lamb` en función de `dt`, `dx` y `k`.

#4. Se establecen los coeficientes `P`, `Q` y `R` de acuerdo con el esquema de diferencias finitas para la ecuación de difusión.

#Este script configura los parámetros y los coeficientes necesarios para resolver una ecuación de difusión unidimensional utilizando un método numérico basado en diferencias finitas. Sin embargo, el método numérico en sí mismo no está implementado aquí. Sería necesario agregar bucles de tiempo y espacio para iterar sobre la región espacial y calcular la temperatura en cada punto en cada paso de tiempo utilizando los coeficientes `P`, `Q` y `R`.
def edpdif(P,Q,R,U,m):
    u=[U[0]]
    for i in range(1,m):
        u=u+[P*U[i-1]+Q*U[i]+R*U[i+1]]    #Calculo de puntos
    u=u+[U[m]]
    return u
from pylab import*
m=11
n=10
Ta=60; Tb=40
To=25
dx=0.1;dt=0.01
L=1
k=4
U=[Ta]
for i in range(1,m):
    u=U+[To]
U=U+[Tb]
lamb=dt/(k*dx**2)
P=lamb
Q=1-2*lamb
R=lamb
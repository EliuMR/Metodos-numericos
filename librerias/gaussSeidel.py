"""Método de Gauss-Seidel para resolver sistemas de ecuaciones lineales \( Ax = f \), donde \( A \) es una matriz cuadrada de tamaño \( n \times n \), \( x \) es el vector de incógnitas y \( f \) es el vector de términos independientes. Aquí hay una descripción de la función `gaussSeidel`:

- `A`: Es la matriz de coeficientes del sistema de ecuaciones lineales.
- `f`: Es el vector de términos independientes.
- `x`: Es el vector de solución inicial. Se actualizará en cada iteración.
- `maxIter`: Es el número máximo de iteraciones permitidas.
- `tol`: Es la tolerancia, es decir, el nivel de precisión deseado para la solución.

El método de Gauss-Seidel resuelve el sistema de ecuaciones lineales iterativamente. En cada iteración, actualiza cada componente de \( x \) utilizando la información de las iteraciones anteriores. Para cada fila \( i \) de la matriz \( A \), se calcula una suma ponderada de las entradas de \( x \) usando los valores actuales de \( x \) (excepto \( x_i \)) y se utiliza esta suma para actualizar \( x_i \). Este proceso se repite hasta que se alcanza una solución dentro de la tolerancia especificada o hasta que se alcanza el número máximo de iteraciones.

La función devuelve el vector \( x \) que representa la solución aproximada del sistema de ecuaciones lineales. Si el método converge dentro del número máximo de iteraciones, se imprime un mensaje indicando el número de iteraciones requeridas para alcanzar la convergencia. Si no converge dentro de las iteraciones máximas, se imprime un mensaje indicando que no convergió.
"""
import numpy 
import numpy.linalg as nl
def gaussSeidel(A,f,x,maxIter=1000,tol=0.001):
    n=f.size
    if (A.shape[0] !=n or A.shape[1] !=n):
        print("Error. Tamaños incompatibles")
        return f
    for iter in range(maxIter):
        res=f-numpy.dot(A,x).flatten()
        if (nl.norm(res,2)<tol):
            print('Converge después de ',iter,'iteraciones')
            return x
        for i in range(n):
            sum=0.0
            for j in range(n):
                if (i!=j):
                    sum +=A[i,j]*x[j]
            x[i]= (f[i]-sum)/A[i,i]
    print('No convergió')
    return x
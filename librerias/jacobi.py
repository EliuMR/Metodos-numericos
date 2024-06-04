    """
    Resuelve un sistema de ecuaciones lineales utilizando el método de Jacobi.

    Args:
        A (numpy.ndarray): Matriz de coeficientes del sistema.
        f (numpy.ndarray): Vector de términos independientes.
        x (numpy.ndarray): Vector de solución inicial.
        maxIter (int): Número máximo de iteraciones permitidas (default=100).
        tol (float): Tolerancia para la convergencia (default=0.0001).

    Returns:
        numpy.ndarray: Vector de solución aproximada.
    """
import numpy
import numpy.linalg as nl
def jacobi(A,f,x,maxIter=100,tol=0.0001):
    n=f.size
    if (A.shape[0] !=n or A.shape[1] !=n):
        print("Error. Tamaños incompatibles")
        return f
    xnew=numpy.copy(x)
    for iter in range(maxIter):
        res=f-numpy.dot(A,x)
        if (nl.norm(res,2)<tol):
            print('Converge después de ',iter,'iteraciones')
            return x
        for i in range(n):
            sum=0.0
            for j in range(n):
                if (i != j):
                    sum +=A[i,j]*x[j]
            xnew [i]= (f[i]-sum)/A[i,i]
        x = numpy.copy(xnew)
    print('No convergió')
    return x
            
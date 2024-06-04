#calcular una aproximación numérica de la integral de una función usando el método del trapecio.

import numpy as np
N=100000
x=np.random.uniform(0,1,size=(1,N))
def f(x):
    return np.exp(-(2.5*x)**2/2.0)
Interaprox=f(x)
Total=5.0*(Interaprox.sum())/(h*np.sqrt(2*np.pi))
print(Total)

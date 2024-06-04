#Resolver una ecuación de difusión unidimensional utilizando un esquema implícito de diferencias finitas. Aquí está una descripción de lo que hace:

#La función edpdifpid toma como entrada los coeficientes P, Q y R que representan la difusividad, la termoconductividad y la fuente de calor respectivamente, junto con la condición inicial U, la derivada en el borde der0, el tamaño del paso espacial dx, y el número de puntos espaciales m.

#Se inicializan las listas a, b, c y d para almacenar los coeficientes de las diagonales de la matriz tridiagonal que surge del esquema implícito de diferencias finitas.

#Se iteran sobre los puntos espaciales interiores, y se asignan los coeficientes P, Q y R a las diagonales correspondientes. Además, se asignan los términos independientes de la ecuación.

#Se ajustan los términos correspondientes a los bordes para tener en cuenta las condiciones de contorno.

#Se resuelve el sistema tridiagonal utilizando la función tridiagonal importada del módulo tridiagonal.

#Se retorna la solución U, que contiene la distribución de temperatura en el material después de un paso de tiempo.

#Este método utiliza un esquema implícito para estabilizar la solución y evitar restricciones en el tamaño del paso temporal en comparación con los métodos explícitos.


from tridiagonal import*
def edpdifpid(P,Q,R,U,der0,dx,m):
    #Método de diferencias finitas  implicito
    a=[];b=[];c=[];d=[]
    for i in range(m-1):
        a=a+[P]
        b=b+[Q]
        c=c+[R]
        d=d+[-U[i+1]]
    c[0]=P+R
    d[0]=d[0]+2*dx*P*der0
    d[m-2]=d[m-2]-c[m-2]*U[m-1]
    u=tridiagonal(a,b,c,d)
    U=u+[U[m-1]]
    return U
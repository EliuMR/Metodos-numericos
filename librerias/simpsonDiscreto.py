#regla de Simpson para integración numérica en un conjunto discreto de puntos. 
#calcula la integral de una función definida en un conjunto discreto de puntos utilizando la regla de Simpson compuesta. La función f debe ser una lista de longitud m+1, donde f[0] es el valor de la función en el punto inicial a, f[m] es el valor de la función en el punto final b, y los valores intermedios representan la función evaluada en los puntos intermedios. La variable m especifica el número de subintervalos en los que se divide el intervalo [a, b] para la integración.
def simpsonDiscreto(f,a,b,m):
    h=1.0*(b-a)/m
    s=0.0
    for i in range(1,m):
        s=s+2*(i%2+1)*f[i]
    s=h/3*(f[0]+s+f[m])
    return s
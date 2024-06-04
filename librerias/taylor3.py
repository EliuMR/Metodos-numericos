#método de Taylor de tercer orden para resolver una ecuación diferencial ordinaria de primer orden.
#Este método utiliza la fórmula de Taylor de tercer orden para aproximar el valor de la función en el siguiente paso de tiempo. El parámetro f es la función que describe la pendiente de la ecuación diferencial, df es la derivada parcial de la función con respecto a y, x e y son las coordenadas del punto inicial, h es el tamaño del paso y m es el número de iteraciones. La función retorna dos listas, una con los valores de x y otra con los valores de y correspondientes a cada paso de tiempo.

#x,y punto inicial
#Iteraciones
def taylor3(f,df,x,y,h,m):
    u=[]
    v=[]
    for i in range(m):
        y=y+h*f(x,y)+h**2/2.0*df(x,y)
        x=x+h
        u=u+[x]
        v=v+[y]
    return [u,v]
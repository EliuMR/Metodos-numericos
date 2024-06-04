#El "método de bisección" es una técnica numérica utilizada para encontrar las raíces de una función continua en un intervalo dado. Este método divide iterativamente el intervalo por la mitad y luego selecciona el subintervalo que contiene la raíz basándose en el cambio de signo de la función en los extremos del intervalo. Este proceso se repite hasta que se alcanza una tolerancia predefinida o se cumple un número máximo de iteraciones.
import numpy as np
def bisectionmethod(h,a,b,maxIter,TOL):
    stop=False
    fa=h(a)
    fb=h(b)
    
    #check starting values
    if(fa*fb>=0):
        print ('error')
    else:
        #Bisection iteration
        for i in range(maxIter):
            c=(a+b)/2
            fc=h(c)
            print("c=",c,"and f(c)",fc)
            
            #check for convergence
            if(np.fabs(fc)<TOL):
                print("Root found at",c)
                stop=True
                break
            #if not conerged, determine end point
            #to replace
            if(fa*fc<0):
                b=c
                fb=fc
            else:
                a=c
                fa=fc
        if stop == False:
            print("Reached maxIter, currently at",c)
    
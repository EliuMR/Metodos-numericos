#Método de eliminación de Gauss para resolver sistemas de ecuaciones tridiagonales.

def tridiagonal(a,b,c,d):
    n=len(d)
    w=[b[0]]
    g=[d[0]/w[0]]
    for i in range(1,n):
        w=w+[b[i]-a[i]*c[i-1]/w[i-1]]
        g=g+[(d[i]-a[i]*g[i-1])/w[i]]
    x=[]
    for i in range(n):
        x=x+[0]
    x[n-1]=g[n-1]
    for i in range(n-2,-1,-1):
        t=x[i+1]
        x[i]=g[i]-c[i]*t/w[i]
    return x
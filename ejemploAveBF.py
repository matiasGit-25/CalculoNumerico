import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

#sistemas lineales en python: sublibreria "linalg"
#x = np.linalg.solve(a, b)

print('\nEjemplo usado: Burden-Faires, página  158, "Ruddy Duck"\n')

print('Este ejemplo/ilustración usa un spine(¿Y en español?)\npara aproximar una curva que no tiene una representación\nfuncional dada.')

#print('defina la función a interpolar por splines cubicos naturales')
## ... ingresa string para pasarle a lambda ... y = lambda x: eval(<str>)
#f = lambda x: np.exp(x) #función del ejemplo de Burden-Faires, página  151, "Example2"
#print(f)
####derivadas de f (con sympy)
####primera
##deriv1 = sym.diff(f(x), x)
####segunda
##deriv2 = sym.diff(deriv1, x)

print('\nInserte n+1 puntos para generar el spline cúbico natural\n')

i = 0
xx = [0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5.0, 6.0, 7.0, 8.0, 9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3]
yy = [1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25]

#¿Cómo podemos insertar la imagen del pato?

#Graficación de los puntos:
x = np.linspace(0, 14, 100)
plt.plot(xx, yy, label='Ruddy Duck')
for _ in range(0, len(xx)):
    plt.scatter(xx[i], yy[i])
plt.show()

##x=input()
##x=(float(x))
##print('x = ',x)
##xx.append(x)
##
##y=input()
##y=float(y)
##print('y(x) = ',f(x))
##yy.append(f(x))
##
##print('¿Más puntos? S/N')
##
##RTA = input()
##if RTA == 'S':
##    seguir = True
##else:
##    seguir = False
##    
##while seguir == True:
##    x=input()
##    x=(float(x))
##    print('x = ',x)
##    xx.append(x)
##    y=input()
##    y=float(y)
##    print('y(x) = ',f(x))
##    yy.append(f(x))
##    print('¿Más puntos? S/N')
##    RTA = input()
##    if RTA == 'S':
##        seguir = True
##    else:
##        seguir = False

print('x\t', xx)
print('f(x)\t', yy)

n = len(xx)
print('hay', n,'puntos, va a haber',n-1,'polinomios para el spline')


## Sistema lineal tridiagonal
## ...

##Crout Factorization for Tridiagonal Linear Systems
##Burden-Faires p 422 (Algorithm 6.7)
##...

def splineCubicoNatural(n, xx, yy):

    #En python hay que simular los arreglos con listas
    #por no existir arrays nativamente
    aa=[]
    aa=yy
    bb=[]
    cc=[]
    dd=[]
    for _ in range(0,n):
        bb.append(0.0)
        cc.append(0.0)
        dd.append(0.0)
    
    #Paso1
    hh = []
    for _ in range(0,n):
        hh.append(0.0)

    for i in range(0,n-1):
        hh[i] = xx[i+1]-xx[i]
        
    #Paso2
    kk = []
    for _ in range(0,n):
        kk.append(0.0)
        
    for i in range(1,n-1):
        kk[i] = ( (3*(yy[i+1]-yy[i])/hh[i]) - (3*(yy[i]-yy[i-1])/hh[i-1]) )
        
    #Paso3
    ll = []
    ll.append(float(1))
    for _ in range(1,n):
        ll.append(0.0)

    mm = []
    mm.append(float(0))
    for _ in range(1,n):
        mm.append(0.0)

    zz = []
    zz.append(float(0))
    for _ in range(1,n):
        zz.append(0.0)
    
    #Paso4
    for i in range(1,n-1):

        ll[i] = 2*(xx[i+1]-xx[i-1]) - hh[i-1]*mm[i-1]

        mm[i] = hh[i]/ll[i]

        zz[i] = (kk[i]-hh[i-1]*zz[i-1])/ll[i]
        
    #Paso5

    #ll[n]=1
    ll.append(float(1))

    #zz[n]=0
    zz.append(float(0))

    #cc[n]=0
    cc.append(float(0))
    
    #Paso6
    for j in range(n-2, -1, -1):

        cc[j] = zz[j]-mm[j]*cc[j+1]
        #cc.insert(0, zz[j]-mm[j]*cc[j+1])

        bb[j] = ( (aa[j+1]-aa[j])/hh[j] - hh[j]*(cc[j+1]+2*cc[j])/3 )
        #bb.append((aa[j+1]-aa[j])/hh[j] - hh[j]*(cc[j+1]+2*cc[j])/3)

        dd[j] = ( (cc[j+1]-cc[j])/(3*hh[j]) )
        #dd.append((cc[j+1]-cc[j])/(3*hh[j]))
        
    #Paso7
    #lista de tuplas
    pp = []
    for j in range(0,n-1):
##Cómo se hace ésto de manera legible para que sea correcto para el intérprete??
##        print(  aa[j] + '+' +
##                bb[j] + '*(x-' + xx[j] + ')' +
##                cc[j] + '*(x-' + xx[j] + ')**2' +
##                dd[j] + '*(x-' + xx[j] + ')**3'
##            )
        print('Polinomio',j+1)
        p = [aa[j], bb[j], cc[j], dd[j]]
        print(p,'\n')
        pp.append(p)
    return(pp)

pp = splineCubicoNatural(n, xx, yy)
#con pp tenemos una lista de tuplas con los coeficientes para los polinomios de spline cúbico
print('Coeficientes del polinomio 1 del spline cúbico:\n',pp[0],'\n')
for i in range(1, len(pp)):
    print('Coeficientes del polinomio',i+1,'del spline cúbico:\n',pp[i],'\n')
#armado de strings de polinomios, los podríamos guardar en una lista, y luego usar eval(pol_i(x)) en equis
#ver el código de la entrega anterior


for i in range(0, len(pp)):
    x = np.linspace(xx[i], xx[i+1], 100)
    print('Polinomio Spline', i+1)
    pol = pp[i] #coeficientes del polinomio
    xj=xx[i]
    Spline=''
    Spline = Spline + str(pol[0])
    for j in range(1, len(pol)):
        #genera string del polinomio de spline
        Spline= Spline+'+('+str(pol[j])+')*(x-'+str(xj)+')**'+str(j)
    plt.plot(x, eval(Spline))    
    print(Spline)
    
plt.show()
        



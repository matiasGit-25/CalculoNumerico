import numpy as np
import matplotlib.pyplot as plt
import math


## interpolacion de lagrange con tabla x, y=f(x)
def lagrange(x, lx, ly):
    y = 0

    for i in range(0, len(lx)):
        L = 1
        for j in range(0, len(lx)):
            if  j != i:
                L = L*(x-lx[j])/(lx[i]-lx[j])
        y = y + L*ly[i]
    return y


## graficadora
def graficadora(val, y, cant, listax, listay):

    # hay que ajustar el rango de x manualmente para cada ejemplo
    print("\nIngrese a del rango de x en [a,b] que se graficará: (ej: 0.1)")
    a=float(input())
    print("a = ", a)
    print("Ingrese b del rango de x en [a,b] que se graficará: (ej: 2)")
    b=float(input())
    print("b = ", b)
    x = np.linspace(a, b, 100)

    # Grafica la funcion original (si es que modelamos una)
##    def f(x):
##        y = <expr>
##        return(float(y))
##    plt.plot(x, f(x), label='funcion interpolada')
    
    # Grafica los datos de la tabla dada
    plt.plot(x, lagrange(x, listax, listay), label="polin. lagrange")
    print("¿Graficar ln(x)? (es el ejemplo propuesto) S/N ")
    rta = str(input())
    while (rta != 'S' and rta != 'N'):
        print("ingrese 'S' para si graficar, 'N' para no graficar")
        rta = str(input())
    if rta == 'S':
        plt.plot(x, np.log(x), label="función interpolada")
    
    for i in range(0, len(listax)):
        plt.scatter(listax[i], listay[i])

    # Grafica el valor deseado que da el pol. interpolado
    y = lagrange(val, listax, listay)
    plt.scatter(val, y, marker="X", label="valor interpolacion")

    # Escribe leyendas
    plt.suptitle('Interpolacion por Polinomio de Lagrange')
    plt.legend()
    
    # Mostrar las lineas mayores de la grilla con lineas gris oscuro
    plt.grid(b=True, which='major', color='#666666', linestyle='-')

    # Mostrar las lineas menores de la grilla con lineas casi transparentes de gris debil
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    plt.show()

    

if __name__ == '__main__':
    
    print ("METODO DE LAGRANGE")
    print("\nejeplo para probar la interpolación:\n")
    print("función: f(x)=ln(x)")
    print("tabla:\nx       |0.25   |0.5    |1      |\nf(x)    |-1.386 |-0.693 |0.0    |\n")
    val = float(input("Valor a interpolar: (ej. 0.3 o 0.7)\n"))
    print ("Valor a interpolar: ", val)
    cant = int(input("Cantidad de pares: (ej.3)\n"))
    print ("Cantidad de pares: ", cant)


    listax=[]
    listay=[]
    # creacion de tabla
    for x in range(cant):
        valor = float(input("Ingrese un valor de x: "))
        listax.append(valor)
        valor = float(input("Ingrese y[x]: "))
        listay.append(valor)

    print("tabla:")
    # imprimimos la listax
    print("x", end='\t|')
    for i in range(0,len(listax)):
        print(listax[i], end='\t|')

    print()
    
    # imprimimos la listay
    print("f(x)", end='\t|')
    for i in range(0,len(listay)):
        print(listay[i], end='\t|')

    print()

    y = lagrange(val, listax, listay)
    print ("\nEl resultado de la interpolacion de Lagrange es: ", y)
    
    # grafica
    graficadora(val, y, cant, listax, listay)
    
    input("Presione una tecla para finalizar")


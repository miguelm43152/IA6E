# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo: 6E
######## CAPITULO 34: Crear y llamar funciones en python ################

import random

# 51.- Crea una función que realice una suma. Para ello,
# tendrás que añadir dos argumentos(numero1 y numero2).
# En su interior, especificarás un print() que muestre el resultado de la suma.
# Deberás hacer tres llamadas que como resultado de la suma den los valores 30, 50 y 57000.
# Los números que introduzcas en la llamada pueden ser los que
# quieras siempre que coincidan los resultados en el print().

##########################################################################
########       Definicion de las funciones necesarias    #################
##########################################################################

def suma( n1:int=0,n2:int=0, *args ):
    res = n1 + n2

    imprime = str(n1) + ' + ' + str(n2) #+ ' = ' + str(res)

    for x in args:
        res = res + x
        imprime += ' + ' + str(x)

    imprime += ' = ' + str(res)

    print( imprime )
    
def sumaLista( a ):
    
    imprime = str(a[0])
    res = a[0]
    for x in range(len(a)-1):
        res = res + a[x+1]
        imprime += ' + ' + str(a[x+1])

    imprime += ' = ' + str(res)

    print( imprime )

def sumaHastaN( n ):
    sumatoria = 0
    a = []
    while sumatoria < n:

      rndNum =random.randrange(1,n)
      if (rndNum + sumatoria) < n:
          a.append( rndNum )
          sumatoria += rndNum
      if ( n - sumatoria ) < int( n * 0.1 ) :
          a.append( n - sumatoria)
          sumatoria = n
    sumaLista(a)

##########################################################################
#######################  Inicio del programa    ##########################
##########################################################################


# una vez definidas nuestras funciones podemos llmarlas para sumar hasta llegar al numero
# que nosotros le pedimos
sumaHastaN(30)
sumaHastaN(50)
sumaHastaN(57000)

sumaHastaN(333)
sumaHastaN(701)
sumaHastaN(1000000)

def sumaMNumerosAleatorios():
    for i in range( random.randrange(1,30) ):
        sumaHastaN( random.randrange( 50,10000) )

# ahora hemos creado una funcion que nos genera numeros
# aleatorios
sumaMNumerosAleatorios()


    

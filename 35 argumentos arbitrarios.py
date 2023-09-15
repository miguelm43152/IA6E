# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo: 6E
######## CAPITULO 35: Argumentos arbitrarios *args ################

# 52.- ¿Cuántos argumentos se utilizan en cada una de estas llamadas?

def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo') #4 argumentos
colores('lila', 'negro', 'rojo') #3 argumentos
colores('rosa') # 1 argumento
colores('marrón', 'naranja') # 2 argumentos

# 53 .- Completa el siguiente fragmento de código:
def colores(*args):
    print('El color', args[-1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')
    print("otros colores que me gustan son:")
    n = len(args)
    a = []
    for i in range(n):
        if i == 0:
            continue
        elif i == n-1:
            continue
        a.append( args[i] )
    else:
        print(a)

colores('amarillo','azul','rosa','marron','naranja','violeta')


# 54.- Crea una función que realice la suma de cinco números utilizando solo *args.
# Debes imprimir el resultado en la consola. La suma no se realizará directamente sobre el print().

def suma( *args ):
    res = 0
    a = ''
    n = len(args)
    for i in args:
        res += i
    print( "El resultado de la suma es:",res)

suma(5,10,15,32)

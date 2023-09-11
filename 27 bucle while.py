# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo 6E
##################### CAPITULO 27: bucle while ###########################################

# 42.- Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5.

x = 0
arreglo = []
while x <= 15:
    arreglo.append(x)
    x += 5
print("Ejercicio 42:",arreglo)
del arreglo, x

# 43.- Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.

x = 0
arreglo = []
while x >= -100:
    arreglo.append(x)
    x -= 20
print('Ejercicio 43:',arreglo)
del arreglo, x

# 44.- Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y que
#      muestre en cada ejecución esta frase con el valor de ejecución correspondiente:
#      'El valor del bucle es 10'...

x = 10
while x >= 0:
    print( 'El valor del bucle es: ' + str(x))
    x -= 1
# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo 6E
##################### CAPITULO 12: Eliminar elementos con del() ###########################################

# 27 De esta lista, elimina los colores 'azul', 'marrón', 'negro' y 'rosa'.
#    Debes utilizar al menos una vez las posiciones negativas para eliminar un color. 
#    Después, imprime la lista para ver los colores que se han eliminado.

import random
ranMun = ( random.randrange(1,10) ) * -1
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colorEliminado = colores[ ranMun ]
del colores[ ranMun ]
print( f"Se eliminó el color {colorEliminado} con índice:", ranMun, "y como resultado se obtuvo:\n ",colores )
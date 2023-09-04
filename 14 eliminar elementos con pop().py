# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo 6E
##################### CAPITULO 14: Eliminar elementos con pop() ###########################################

# 28 Elimina de la siguiente lista los elementos 'azul' y 'blanco'.
#    Solo puedes eliminarlos utilizando el método pop().
#    Además, tendrás que guardar esos dos colores en una nueva lista.

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

elementosEliminados = [colores.pop(1), colores.pop(-2)]

print( f"se eliminaron los colores {elementosEliminados[0]} y {elementosEliminados[1]} de la lista:\n{colores}" )
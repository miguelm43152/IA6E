# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo 6E
##################### CAPITULO 17: Ordenar elementos con sort() y sorted() ########################################

# 32  Ordena la siguiente lista en orden alfabético descendente (de la letra 'z' a la 'a').

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón',
'lila', 'negro', 'rosa', 'blanco', 'naranja']

# sorted es un cambio temporal del arreglo, por lo que no altera realmente el orden de nuestra lista
print( sorted(colores, reverse=False) )
print( sorted(colores, reverse=True), "\n" )

#imprimiremos de nuevo la lista para observar que no ha sido alterada realmente:

print( colores, "\n")

#En cambio, sort() sí que hace cambios permanentes en nuestra lista como veremos a continuación:
colores.sort(  )
print( colores )
colores.sort( reverse= True )
print( colores, '\n' )
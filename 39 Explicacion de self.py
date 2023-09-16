# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo: 6E
############ CAPITULO 39: Explicacion de Self ####################

# En este caso en lugar de escribir la palabra self, hacemos referencia al mismo objeto
# con otro nombre. En el caso del primer método usamos la palabra "usuario" y para el segundo
# método usamos la palabra "datos"
#
# Concluímos entonces que, no es necesario nombrar al objeto 'self' sino que podemos
# usar cualquier otro nombre que queramos usar para referrirnos al propio objeto

class Usuarios:
    def __init__(usuario, nombre, edad):
        usuario.nombre = nombre
        usuario.edad = edad

    def muestraDatos(datos):
        print("El nombre de usuario es:", datos.nombre, "su edad es:",datos.edad)

usuario1 = Usuarios( "Julián", 56)
usuario1.muestraDatos()

usuario1.edad = 65

usuario1.muestraDatos()

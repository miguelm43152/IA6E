# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo: 6E
############ CAPITULO 40: Declarar clases vacías con pass ####################
############                y eliminar objetos            ####################

class Coches():
    pass

class Colores():
    pass
  
class Patos():
    pass

coche1 = Coches()

class Usuarios:
    def __init__(usuario, nombre, edad):
        usuario.nombre = nombre
        usuario.edad = edad

    def muestraDatos(self):
        print( "El nombre de usuario es:", self.nombre, "la edad es:", self.edad)

usuario1 = Usuarios( "Enrique", 28)
usuario2 = Usuarios( "Carlos", 32)

usuario1.muestraDatos()
usuario2.muestraDatos()

del usuario1.edad
del usuario2

#usuario1.muestraDatos()
usuario2.muestraDatos()

# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo: 6E
############    CAPITULO 42: Herencia de __init__      ####################

class Usuarios:
    def __init__(usuario, nombre, edad):
        usuario.nombre = nombre
        usuario.edad = edad

    def muestraDatos(self):
        print( "El nombre de usuario es:", self.nombre, "la edad es:", self.edad)


# Esta es la manera que se tiene para realizar la herencia de clases en python
class Usuarios_premium( Usuarios ):
    def __init__(usuario,nombre,edad,instagram):
        Usuarios.__init__(usuario,nombre,edad)
#        usuario.nombre = nombre
#        usuario.edad = edad
        usuario.instagram = instagram

    def muestraDatos(self):
        print( "El nombre de usuario es:", self.nombre, "la edad es:", self.edad, "Su insta es:", self.instagram)

usuario1 = Usuarios("Joaquín", 42);
usuario1.muestraDatos();

usuario2 = Usuarios_premium( "Luis", 53, "Luis@ins.com");
usuario2.muestraDatos();

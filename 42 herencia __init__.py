# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo: 6E
############    CAPITULO 42: Herencia de __init__      ####################

####################################################################################################################################
############################################# Definicion de clases #################################################################
####################################################################################################################################


################################################# Clase Padre ######################################################################

class Usuarios:
    ##### Constructor #######
    def __init__(usuario, nombre, edad):
        usuario.nombre = nombre
        usuario.edad = edad

    ##### Metodos #######
    def muestraDatos(self):
        print( "El nombre de usuario es:", self.nombre, "la edad es:", self.edad)


################################################# Clase Hija ######################################################################

# Esta es la manera que se tiene para realizar la herencia de clases en python
class Usuarios_premium( Usuarios ):
    ### se llama al constructor de la clase padre #####
    def __init__(usuario,nombre,edad,instagram):
        Usuarios.__init__(usuario,nombre,edad)

        #con la línea anterior nos ahorramos estas dos lineas porque llamamos el constructor heredado
        # que ya contiene estas dos lineas siguientes (ver el constructor de la clase padre)
#        usuario.nombre = nombre
#        usuario.edad = edad
        usuario.instagram = instagram

    ### metodos #####
    def muestraDatos(self):
        print( "El nombre de usuario es:", self.nombre, "la edad es:", self.edad, "Su insta es:", self.instagram)

####################################################################################################################################
############################################# Programa principal #################################################################
####################################################################################################################################


usuario1 = Usuarios("Joaquín", 42);
usuario1.muestraDatos();

usuario2 = Usuarios_premium( "Luis", 53, "Luis@ins.com");
usuario2.muestraDatos();

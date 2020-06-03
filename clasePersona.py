class Persona:
    __Nombre = ''
    __Direccion = ''
    __Dni = ''

    def __init__(self,nombre,direccion,dni):
        self.__Nombre = nombre
        self.__Direccion = direccion
        self.__Dni = dni

    def getDni(self):
        return self.__Dni

    def __str__(self):
        return 'Nombre: '+ self.__Nombre+'\n Direccion: '+self.__Direccion+'\n Dni: '+self.__Dni

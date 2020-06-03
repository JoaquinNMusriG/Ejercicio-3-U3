class TallerCapacitacion:
    __IDTaller = 0
    __Nombre = ''
    __Vacantes = 0
    __MontoInscripcion = 0

    def __init__ (self,id,nom,vacantes,monto):
        self.__IDTaller = id
        self.__Nombre = nom
        self.__Vacantes = vacantes
        self.__MontoInscripcion = monto

    def __str__ (self):
        return 'Id: '+str(self.__IDTaller)+' Nombre: '+self.__Nombre+' Vacantes: '+str(self.__Vacantes)+' Monto Inscripcion: '+str(self.__MontoInscripcion)

    def getID (self):
        return self.__IDTaller

    def getVacantes(self):
        return self.__Vacantes

    def actualizarVacantes(self):
        self.__Vacantes -= 1

    def getNom(self):
        return self.__Nombre

    def getMonto(self):
        return self.__MontoInscripcion

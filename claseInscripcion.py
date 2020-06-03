class Inscripcion:
    __FechaInscripcion = None
    __Pago = False
    __Persona = None
    __Taller = None

    def __init__ (self, fecha, persona, taller):
        self.__FechaInscripcion = fecha
        self.__Persona = persona
        self.__Taller = taller
        self.__Pago = False

    def getPer (self):
        return self.__Persona

    def getPago(self):
        return self.__Pago

    def getTal (self):
        return self.__Taller

    def pagado(self):
        self.__Pago = True

    def getFecha(self):
        return self.__FechaInscripcion

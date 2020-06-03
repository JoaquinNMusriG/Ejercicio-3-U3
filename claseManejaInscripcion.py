from claseInscripcion import Inscripcion
import numpy as np

class ManejaInscripciones:
    __inscripciones = np.empty(0)

    def __init__(self):
        self.__inscripciones = np.empty(0)

    def inscribirPersona (self,fecha,persona,taller):
        unaInscripcion = Inscripcion(fecha,persona,taller)
        self.__inscripciones = np.append(self.__inscripciones,unaInscripcion)

    def getTotalInsc(self):
        return self.__inscripciones.size

    def getPersona(self,i):
        return self.__inscripciones[i].getPer()

    def verificarPago(self,i):
        resultado = False
        if self.__inscripciones[i].getPago():
            resultado = True
        return resultado

    def getTaller(self,i):
        return self.__inscripciones[i].getTal()

    def registrarPago(self,i):
        self.__inscripciones[i].pagado()

    def FECHA(self,i):
        return self.__inscripciones[i].getFecha()

    def PAGO(self,i):
        return self.__inscripciones[i].getPago() 

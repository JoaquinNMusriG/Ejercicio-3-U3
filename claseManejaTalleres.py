from claseTallerCapacitacion import TallerCapacitacion
import csv
import numpy as np

class ManejaTalleres:
    __talleres = np.empty(0)

    def __init__(self):
        archivo = open('Talleres.csv')
        reader= csv.reader(archivo,delimiter=',')
        cant = int(next(reader)[0])
        self.__talleres = np.empty(cant, dtype = TallerCapacitacion)
        for i in range(cant):
            taller= next(reader)
            unTaller = TallerCapacitacion(int(taller[0]),taller[1],int(taller[2]),int(taller[3]))
            self.__talleres[i] = unTaller

    def mostrarTalleres(self):
        for taller in self.__talleres:
            print(taller)

    def buscarID (self,id):
        band = False
        indice = 0
        while (indice < self.__talleres.size) & (not band):
            if (self.__talleres[indice].getID() == id):
                band = True
            else:
                indice += 1
        if indice < self.__talleres.size:
            resultado = self.__talleres[indice]
        else:
            resultado = None
        return resultado

    def verificarVacantes(self,taller):
        resultado = True
        if taller.getVacantes() == 0:
            resultado = False
        else:
            taller.actualizarVacantes()
        return resultado

    def mostrarTallerYMonto(self,taller,pago):
        print('Nombre del taller: '+taller.getNom())
        if (pago):
            print('Monto que adeuda: 0')
        else:
            print('Monto que adeuda: '+ str(taller.getMonto()))

    def verificarID(self,taller,id):
        resultado = False
        if taller.getID() == id:
            resultado = True
        return resultado

    def ID (self,unTaller):
        return unTaller.getID()    

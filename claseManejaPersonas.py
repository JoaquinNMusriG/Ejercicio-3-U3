from clasePersona import Persona

class ManejaPersonas:
    __personas = []

    def __init__(self):
        self.__personas = []

    def agregarUnaPerona (self):
        resultado = True
        nombre = input('Ingrese el nombre de la persona: ')
        if nombre.isalpha():
            direccion = input('Ingrese la dirección de la persona: ')
            dni = input('Ingrese el dni de la persona: ')
            if dni.isdigit():
                unaPersona = Persona(nombre,direccion,dni)
                self.__personas.append(unaPersona)
            else:
                    resultado = False
                    print('DNI inválido.')
        else:
            resultado = False
            print('NOMBRE inválido.')
        return resultado

    def cargarPersonas(self):
        salir = False
        while not salir:
            print("""
                0 Salir
                1 Agregar Persona""")
            op = input('Ingrese una opcion: ')
            if op == '1':
                resultado = self.agregarUnaPerona()
                if not resultado:
                    print('No se agrego la persona.')
            salir = op == '0'

    def buscarDNI(self,dni):
        band = False
        indice = 0
        while (indice < len(self.__personas)) & (not band):
            if (self.__personas[indice].getDni() == dni):
                band = True
            else:
                indice += 1
        if indice < len(self.__personas):
            resultado = self.__personas[indice]
        else:
            resultado = None
        return resultado

    def verificarDNI(self,persona,dni):
        resultado = False
        if persona.getDni() == dni:
            resultado = True
        return resultado

    def mostrarDatos(self,persona):
        print(persona)

    def DNI (self,unaPersona):
        return unaPersona.getDni()    

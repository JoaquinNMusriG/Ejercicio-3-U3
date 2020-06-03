from claseManejaTalleres import ManejaTalleres
from claseManejaPersonas import ManejaPersonas
from claseManejaInscripcion import ManejaInscripciones
import csv
import datetime

if __name__ == '__main__':
    talleres = ManejaTalleres()                   #cargar talleres

    personas = ManejaPersonas()
    personas.cargarPersonas()                   #cargar personas

    print('-------------')

    inscripciones = ManejaInscripciones()
    salir = False
    while not salir:
        print("""
            0 Salir
            1 Inscribir Persona""")
        op = input('Ingrese una opcion: ')
        if op == '1':
            dni = input('Ingrese el dni de la persona a inscribir: ')
            if dni.isdigit():
                persona = personas.buscarDNI(dni)
                if persona != None:
                    id = input('Ingrese el id del taller donde se inscribira dicha persona: ')
                    if id.isdigit():
                        taller = talleres.buscarID(int(id))
                        if taller != None:
                            if talleres.verificarVacantes(taller):
                                fecha = datetime.date.today()         #Inscribir persona
                                inscripciones.inscribirPersona(fecha,persona,taller)
                            else:
                                print('No hay vacantes disponibles para ese taller')
                        else:
                            print('No hay registro de ese taller.')
                    else:
                        print('Valor inválido de taller.')
                else:
                    print('No hay registro de esa persona.')
            else:
                print('Valor inválido de persona.')
        salir = op == '0'

    print('-------------')

    dni = input('Ingrese el dni de la persona a consultar inscripcion: ')
    if dni.isdigit():
        band = False
        i = 0
        while (i < inscripciones.getTotalInsc()):
            persona = inscripciones.getPersona(i)
            if personas.verificarDNI(persona,dni):
                pago = inscripciones.verificarPago(i)
                taller = inscripciones.getTaller(i)                             #mostrar talleres de persona inscripta
                talleres.mostrarTallerYMonto(taller,pago)
                band = True
            i += 1
        if not band:
            print('No hay registro de esa persona en los inscriptos.')
    else:
        print('Dni inválido.')

    print('-------------')

    id = input('Ingrese el id del taller al cual listar los alumnos: ')
    if id.isdigit():
        band = False
        i = 0
        while (i < inscripciones.getTotalInsc()):
            taller = inscripciones.getTaller(i)
            if talleres.verificarID(taller,int(id)):
                persona = inscripciones.getPersona(i)                     #mostrar alumnos de un taller
                personas.mostrarDatos(persona)
                band = True
            i += 1
        if not band:
            print('No hay registro de inscriptos.')
    else:
        print('ID inválido')

    print('-------------')

    dni = input('Ingrese el dni de la persona que acreditó el pago: ')
    if dni.isdigit():
        band = False
        i = 0
        while (i < inscripciones.getTotalInsc()):
            persona = inscripciones.getPersona(i)
            if personas.verificarDNI(persona,dni):                      #registrar pago de los talleres que asiste la persona
                inscripciones.registrarPago(i)
                band = True
            i += 1
        if not band:
            print('No hay registro de esa persona en los inscriptos.')
    else:
        print('Dni inválido.')

    print('-------------')

    print('Guardando información')
    archivo= open('Inscriptos.csv','w',newline ='')
    salida= csv.writer(archivo,delimiter = ';')                     #Guardar información
    salida.writerow(['dni','idTaller','fecha','pago'])
    for i in range(inscripciones.getTotalInsc()):
        persona= inscripciones.getPersona(i)
        taller = inscripciones.getTaller(i)
        dni = personas.DNI(persona)
        id = talleres.ID(taller)
        fecha = inscripciones.FECHA(i)
        pago = inscripciones.PAGO(i)
        row=[dni,id,fecha,pago]
        salida.writerow(row)

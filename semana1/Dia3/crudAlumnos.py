import tabulate
#from libAlumnos import menu,buscarAlumnos
#from libAlumnos import (menu,buscarAlumnos) -> para varias funciones de la liberia
from libAlumnos import *

menu()
opcion = 0
# alumnos = [{'nombre':'Paul Moreno','email':'prueba@gmail.com','celular':'999999999'}]
#cargamos datos del archivo de texto
f = open('alumnos.txt','r')
strAlumnos = f.read()
alumnos = cargarAlumnos(strAlumnos)
f.close

while(opcion != 5):
    opcion = int(input("INGRESE OPCION DEL MENU : "))
    if(opcion == 1):
        print("NUEVO ALUMNO")
        insertarAlumno(alumnos)
    elif(opcion == 2):
        print("RELACION DE ALUMNOS")
        cabeceras = alumnos[0].keys()
        registros = [x.values() for x in alumnos]
        print(tabulate.tabulate(registros,cabeceras))
    elif(opcion == 3):
        print("ACTUALIZAR ALUMNO")
        #PASO 1 BUSCAR EL ALUMNO A EDITAR
        valorBusqueda = input("Ingrese el email del almuno a actualizar : ")
        indexAlumno = buscarAlumnos(valorBusqueda,alumnos)
        if(indexAlumno == -1):
            print("No se encontró el email del alumno")
        else:
            actualizarAlumno(indexAlumno,alumnos)
            print("ALUMNO ACTUALIZADO")
    elif(opcion == 4):
        print("ELIMINAR ALUMNO")
        valorBusqueda = input("Ingrese el email del almuno a eliminar : ")
        indexAlumno = buscarAlumnos(valorBusqueda,alumnos)
        if(indexAlumno == -1):
            print("No se encontró el email del alumno")
        else:
            eliminarAlumno(indexAlumno,alumnos)
            print("ALUMNO ELIMINADO")
    elif(opcion == 5):
        #Grabar los datos en mi archivo de texto
        strAlumnos = grabarAlumnos(alumnos)
        #print(strAlumnos)
        fw = open('alumnos.txt','w')
        fw.write(strAlumnos)
        fw.close
        print("FINALIZANDO PROGRAMA")
    else:
        print("OPCION INCORRECTA")
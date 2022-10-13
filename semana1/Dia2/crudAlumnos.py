import tabulate

print("-" * 50)
print("|" + " " * 9 + "MATRICULA DE ALUMNOS EN CODIGO" + " " * 9 + "|")
print("-" * 50)
print("|" + " " * 9 + "MENU DE OPCIONES     " + " " * 18 + "|")
print("|" + " " * 9 + "[1] REGISTRAR ALUMNO " + " " * 18 + "|")
print("|" + " " * 9 + "[2] MOSTRAR ALUMNO   " + " " * 18 + "|")
print("|" + " " * 9 + "[3] ACTUALIZAR ALUMNO" + " " * 18 + "|")
print("|" + " " * 9 + "[4] ELIMINAR ALUMNO  " + " " * 18 + "|")
print("|" + " " * 9 + "[5] SALIR            " + " " * 18 + "|")
print("-" * 50)
opcion = 0
alumnos = [{'nombre':'Paul Moreno','email':'prueba@gmail.com','celular':'999999999'}]
while(opcion != 5):
    opcion = int(input("INGRESE OPCION DEL MENU : "))
    if(opcion == 1):
        print("NUEVO ALUMNO")
        nombre = input("NOMBRE   : ")
        email = input("EMAIL     : ")
        celular = input("CELULAR : ")
        dictAlumno = {
            'nombre':nombre,
            'email':email,
            'celular':celular
        }
        alumnos.append(dictAlumno)
        print("ALUMNO REGISTRADO CON ÉXITO")
    elif(opcion == 2):
        print("RELACION DE ALUMNOS")
        cabeceras = alumnos[0].keys()
        registros = [x.values() for x in alumnos]
        print(tabulate.tabulate(registros,cabeceras))
    elif(opcion == 3):
        print("ACTUALIZAR ALUMNO")
        #PASO 1 BUSCAR EL ALUMNO A EDITAR
        valorBusqueda = input("Ingrese el email del almuno a actualizar : ")
        indexAlumno = -1
        for i in range(len(alumnos)):
            dictAlumnoBusqueda = alumnos[i]
            for clave,valor in dictAlumnoBusqueda.items():
                if(valor == valorBusqueda and clave == 'email'):
                    indexAlumno = i
                    break
        #print("El alumno esta en el indice : " + str(indexAlumno))
        #print("datos del alumno :" + str(alumnos[indexAlumno]))
        #PASO 2 INGRESAR LOS NUEVOS VALORES PARA EL ALUMNO A EDITAR
        if(indexAlumno == -1):
            print("No se encontró el email del alumno")
        else:
            nombre = input("NOMBRE   : ")
            email = input("EMAIL     : ")
            celular = input("CELULAR : ")
            dictAlumnoEditar = {
                'nombre':nombre,
                'email':email,
                'celular':celular
            }
             #PASO 3 ACTUALIZAR LOS DATOS DEL ALUMNO A EDITAR
            alumnos[indexAlumno] = dictAlumnoEditar
            print("ALUMNO ACTUALIZADO")
    elif(opcion == 4):
        print("ELIMINAR ALUMNO")
        valorBusqueda = input("Ingrese el email del almuno a eliminar : ")
        indexAlumno = -1
        for i in range(len(alumnos)):
            dictAlumnoBusqueda = alumnos[i]
            for clave,valor in dictAlumnoBusqueda.items():
                if(valor == valorBusqueda and clave == 'email'):
                    indexAlumno = i
                    break
        if(indexAlumno == -1):
            print("No se encontró el email del alumno")
        else:
            alumnos.pop(indexAlumno)
            print("ALUMNO ELIMINADO")
    elif(opcion == 5):
        print("FINALIZANDO PROGRAMA")
    else:
        print("OPCION INCORRECTA")
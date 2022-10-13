#LIBRERIA DE ALUMNOS
def menu():
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
    
def insertarAlumno(alumnos):
    nombre = input("NOMBRE : ")
    email = input("EMAIL  : ")
    celular = input("CELULAR: ")
    dictAlumno = {
        'nombre':nombre,
        'email':email,
        'celular':celular
    }
    alumnos.append(dictAlumno)
    print("ALUMNO REGISTRADO CON ÉXITO")
    
def buscarAlumnos(valorBusqueda,alumnos):
    indexAlumno = -1
    for i in range(len(alumnos)):
        dictAlumnoBusqueda = alumnos[i]
        for clave,valor in dictAlumnoBusqueda.items():
            if(valor == valorBusqueda and clave == 'email'):
                indexAlumno = i
                break
    return indexAlumno

def actualizarAlumno(indexAlumno,alumnos):
    nombre = input("NOMBRE : ")
    email = input("EMAIL  : ")
    celular = input("CELULAR: ")
    dictAlumnoEditar = {
        'nombre':nombre,
        'email':email,
        'celular':celular
    }
    alumnos[indexAlumno] = dictAlumnoEditar

def eliminarAlumno(indexAlumno,alumnos):
    alumnos.pop(indexAlumno)

def cargarAlumnos(strAlumnos):
    # convierte un string a una lista de diccionarios
    alumnos = []
    #PROCESO PAR ACONVERTIR UNA CADENA STRING A UNA LISTA DE DICCIONARIOS
    listaAlumnos = strAlumnos.splitlines()
    for l in listaAlumnos:
        alumnoData = l.split(',')
        l = {
            'nombre': alumnoData[0],
            'email': alumnoData[1],
            'celular': alumnoData[2]
        }
        alumnos.append(l)
    return alumnos

def grabarAlumnos(alumnos):
    #convierte una lista de diccionarios en un string
    strAlumnos = ""
    for l in alumnos:
        for clave,valor in l.items():
            strAlumnos += valor
            if(clave != 'celular'):
                strAlumnos += ','
            else:
                strAlumnos += '\n'
    return strAlumnos
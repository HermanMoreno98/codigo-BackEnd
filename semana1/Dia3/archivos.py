# f = open('alumnos.txt','w')
# f.write('paul moreno,pmoreno@gmail.com,23456778\n')
# f.write('ana lopez,alopez@gmail.com,23456778\n')
# f.write('jorge perez,jperez@gmail.com,23456778')

f = open('alumnos.txt','r')
alumnos = f.read()
print(alumnos)

listaAlumnos = alumnos.splitlines()
print(listaAlumnos)

listaResultado = []
for dictAlumno in listaAlumnos:
    listaDiccionarioAlumnos = dictAlumno.split(',')
    print(listaDiccionarioAlumnos)
    dictAlumno = {
        'nombre': listaDiccionarioAlumnos[0],
        'email': listaDiccionarioAlumnos[1],
        'celular': listaDiccionarioAlumnos[2]
    }
    listaResultado.append(dictAlumno)
print(listaResultado)
f.close
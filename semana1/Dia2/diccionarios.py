# Similar a JSON
capitales = {
   'Perú':'Lima',
    'Ecuadro':'Quito',
    "Chile":"Santiago",
    "Uruguay":"Montevideo"
}
print(capitales)
#Agregando valores el formulario
nuevaCapital = {'Brasil':'Brasilia'}
capitales.update(nuevaCapital)
print(capitales)
#Eliminar valores del diccionario
c = capitales.pop('Chile')
print(c)

#### BASE DE DATOS DE ALUMNOS ####
alumno1 = {
    'Nombre':'César Mayta',
    'Edad': 39,
    'Nota': 19.5,
    'aprobado':True,
    'cursos':['javascript','python','C#']
}
alumno2 = {
    'Nombre':'Lucia Torres',
    'Edad': 29,
    'Nota': 20,
    'aprobado':True,
    'cursos':['javascript','Swift','Kotlin']
}

alumnos = [alumno1,alumno2]
print(alumnos)

# Iteraciones
for capital in capitales:
    print(capital + " : " + capitales[capital])
print(capitales.keys())
print(capitales.values())
for clave in capitales.keys():
    print(clave + " => " + capitales[clave])
for clave,valor in capitales.items():
    print(clave + " -- " + valor)
    

for alumno in alumnos:
    for clave,valor in alumno.items():
        print(valor, end=' |  ')
    print()
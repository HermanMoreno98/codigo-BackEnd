## Tabla de multiplicar
tabla = int(input("Ingresa la tabla de multiplicar que desea mostrar: "))

for contador in range(1,41):
    valor = tabla * contador
    print(str(tabla) + " x " + str(contador) + " = " + str(valor))
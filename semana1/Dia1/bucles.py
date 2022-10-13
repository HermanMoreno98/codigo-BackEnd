opcion = 0
while(opcion == 0):
    print(" ========== OPCIONES ==========")
    print(" 1) opcion 01")
    print(" 2) opcion 02")
    print(" 3) opcion 03")
    opcion = int(input("opcion elegida: "))
    print("Usted eligió la opcion " + str(opcion))
    salir = input("¿Desea salir? (si/no)")
    if(salir == "no"):
        opcion = 0
    else:
        opcion = -1
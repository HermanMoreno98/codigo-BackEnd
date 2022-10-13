# PROGRAMA PARA CONVERTIR MONEDAS
print("Bienvenido al programa de conversión de monedas");
menu = "";
while menu == "":
    monto = float(input("Ingrese el monto: "));
    opcion = "";
    while(opcion == ""):
        print("¿Qué operación desea realizar?");
        print("1. Conversión de soles a dolares");
        print("2. Conversión de dolares a soles");
        opcion = int(input("Seleccione una opción: "));
        tipoCambio = 3.8;
        if(opcion == 1):
            montoDolares = monto / tipoCambio;
            montoDolaresFormato = "$ {:,.2f}".format(montoDolares);
            print("El monto en dólares es : " + str(montoDolaresFormato));
        elif(opcion == 2):
            montoSoles = monto * tipoCambio;
            montoSolesFormato = "S/. {:,.2f}".format(montoSoles);
            print("El monto en soles es : " + str(montoSolesFormato));
        else:
            print("Error, seleccione una opción válida");
            opcion = "";
    print("¿Desea continuar en la aplicacion?")
    print("1. Si");
    print("2. No");
    opcion2 = int(input("Seleccione una opción"));
    if(opcion2 == 1):
        opcion2 = menu;
    else:
        menu = -1;




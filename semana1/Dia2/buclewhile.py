n = int(input("Ingresa la tabla de multiplicar que desea: "))
i = 1
while(i <= 10):
    valor = n * i
    print(str(n) + " x " + str(i) + " = " + str(valor))
    i+=1

lado = int(input("Ingrese el lado del cuadrado"))
i=1
while(i<=lado):
    if(i==1 or i==lado):
        print("* " * lado)
    else:
        print("* "+("  "*(lado-2))+"*")
    i+=1
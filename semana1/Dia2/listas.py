dias = ["lunes","martes","miercoles"]
print(dias)
print(dias[0])
print(dias[1:2])
dias.append("jueves")
print(dias[1:3])
dias.pop()
print(dias)
dias[0] = "domingo"
print(dias)

for dia in dias:
    print("hoy es " + dia)
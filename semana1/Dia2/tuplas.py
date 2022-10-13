dias = ("lunes","martes","miercoles","jueves","viernes")

print(dias)
# Las tuplas se deben usar cuando sabemos la cantidad de valores de una variable
dias = list(dias)
dias.append("sabado")
print(dias)
dias = tuple(dias)
print(dias)
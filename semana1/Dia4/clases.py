#Crear clase
class Automovil:
    #crear atributos
    def __init__(self,aa,pl,col,mar):
        self.anio = aa
        self.placa = pl
        self.color = col
        self.marca = mar
    
    def encender(self):
        print('Encender '+self.marca)
    
    def avanzar(self):
        print('Avanzar '+self.marca)
    
    def acelerar(self):
        print('Acelerar '+self.marca)
    
    def frenar(self):
        print('Frenar '+self.marca)

#Creacion de objetos
vw = Automovil(1970,'CH-1234','Amarillo','VolksWagen')
print('Se creó el objeto vw con los datos: ')
print("Año  : "+str(vw.anio))
print("Placa: "+vw.placa)
print("Color: "+vw.color)
print("Marca: "+vw.marca)
print("")
#Utilizar objetos
vw.encender()
vw.frenar()
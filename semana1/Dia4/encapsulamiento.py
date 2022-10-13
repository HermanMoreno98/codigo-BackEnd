#Clase para administrar los usuarios de un sistema
class Usuario:
    def __init__(self,nom,pwd):
        self.nombre = nom
        self.__password = pwd
    
    def iniciarSesion(self):
        if(self.nombre == 'admin' and self.__password == '12345'):
            print('Bienvenido ' + self.nombre)
        else:
            print('Datos de acceso incorrectos')

usuarioA = Usuario('admin','admin')
usuarioB = Usuario('admin','12345')

usuarioA.iniciarSesion()
usuarioB.iniciarSesion()





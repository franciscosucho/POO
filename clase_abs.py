from abc import ABC, abstractclassmethod
#Cuando le pasasmos ABC como parametros a una clase
#significa que le estamos diciendo que va a hacer abstracta

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,trabajo):
        self.nombre= nombre
        self.edad= edad
        self.trabajo=trabajo
    
    #creamos un metodo abstracto
    @abstractclassmethod
    def trabajar(self):
        #no le definimos nada, para que las clases que hereden 
        #puedan definirlo
        pass
    def hola(self):
        print(f"Hola, soy: {self.nombre} y trabajo de {self.trabajo}")

class trabajardor(Persona):
    def __init__(self,nombre,edad,trabajo,sueldo):
        super().__init__(nombre,edad,trabajo)
        self.sueldo=sueldo
    def trabajar(self):
        print(f"Trabajo en el rubro de :{self.trabajo} y mi sueldo es: {self.sueldo}")

fran =trabajardor("francisco",18,"programador",18000)
fran.trabajar()
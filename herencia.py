# CLASE PADRE

class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionaldiad = nacionalidad
    def hablar(self):
        print("HOLA")
        

#       HERENCIA SIMPLE
#       CLASE HIJA
class Empleado(Persona):
    #este __init__ nos sirve para decir todos los atributos iniciales que tendra la clase
    def __init__(self, nombre, edad, nacionalidad,trabajo,salario):
        # super( ) es el metodo para que la clase herede los atributos.
        super().__init__(nombre, edad, nacionalidad)
        #abajo ponemos los atributos que va aatener la nueva clase
        self.trabajo = trabajo
        self.salario = salario

ana= Empleado("ana",49,"argentina","prog",10000)

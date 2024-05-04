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
class Empleado():
    #este __init__ nos sirve para decir todos los atributos iniciales que tendra la clase
    def __init__(self,trabajo,salario):
        self.trabajo = trabajo
        self.salario = salario
        
#Va a tener una herencia de dos clases
class Estudiante(Persona, Empleado):
    #este __init__ nos sirve para decir todos los atributos iniciales que tendra la clase
    def __init__(self, nombre, edad, nacionalidad,trabajo,salario,curso,escuela):
        #Las clases que heredamos
        Persona.__init__(self,nombre, edad, nacionalidad)
        Empleado.__init__(self,trabajo,salario)
        #abajo ponemos los atributos que va aatener la nueva clase
        self.curso = curso
        self.escuela = escuela
    def presentarse(self):
        print(  f'{super().hablar()} mi nombre es: {self.nombre}')

fran= Estudiante("Fran","18","arg","prog",10000,"6to 3ra","tec 1")
fran.presentarse()   # Imprime el resultado del metodo presentarse

#Metodo para ver si una clase es una sub clase de otra
# si dice que es true, es por que es una sub clase
herencia=issubclass(Estudiante,Persona)

#Metodo para ver si un objeto es una instancia de una clase.
instancia= isinstance(fran,Empleado)
print(instancia)
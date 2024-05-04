class Persona():
    #Este tambien es un metodo dunder
    def __init__(self,nombre,edad) :
        self.nombre = nombre
        self.edad = edad
    #Este es un operador dunder que nos sirve para decirle a py como tiene que mostrar al objeto cuando lo llamemos
    def __str__(self) :
        return f"persona({self.nombre},{self.edad})"
    def __add__(self,obj):
        nuevo_valor= self.edad+ obj.edad
        return Persona(self.nombre+"|"+ obj.nombre, nuevo_valor)


fran= Persona("fran",18)
pedro= Persona("pedro",18)
juan = Persona("juan",18)
nueva_persona=fran+pedro+juan
print(nueva_persona)
""" El polimorfismo es la capacidad que tienen algunos lenguajes 
    Para hacer que dos objetos distintos, con clases distintas
    pero que comparten el mismo nombre de metodo, puedan hacer cosas distintas.
"""
class Perro:
    def sonido():
        return "Miua"
         
class Gato:
    def sonido():
        return "Guao" 
    
perro=Perro()     
gato=Gato()
print(Perro.sonido())
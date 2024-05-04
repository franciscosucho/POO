from abc import ABC, abstractclassmethod


# class Trabajador(ABC):
#     @abstractclassmethod
#     def Trabajar(self):
#         pass
#     @abstractclassmethod
#     def Dormir(self):
#         pass
#     @abstractclassmethod
#     def Comer(self):
#         pass
#lo que hacemos aca es separar las interfaces, para que cada una cumpla una funcion
class Trabajador(ABC):
    @abstractclassmethod
    def Trabajar(self):
        pass
class Durmiente(ABC):
    @abstractclassmethod
    def Dormir(self):
        pass
class Comedor(ABC):
    @abstractclassmethod
    def Comer(self):
        pass
class Humano(Trabajador,Comedor,Durmiente):
    def Comer(self):
        print("El humano come") 
        
    def Trabajar(self):
        print("El humano Trabaja") 
        
    def Dormir(self):
        print("El humano Duerme") 

class Robot(Trabajador):
      def Trabajar(self):
        print("El humano Trabaja") 
robot1= Robot()

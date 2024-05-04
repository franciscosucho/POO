class Tanque():
    def __init__(self):
        self.combustible=100
    def agregar_com(self,cantidad):
        self.combustible +=cantidad
    def ob_com(self):
        return self.combustible
    def usar_com(self,cantidad):
        self.combustible -=cantidad
    
class Auto():
    def __init__(self,tanque):
        self.posicion = 0
        self.tanque = tanque
        
    def mover(self, distancia):
        if self.tanque.ob_com() >= distancia/2:
            self.posicion += distancia
            self.tanque.usar_com(distancia/2)
            print(f"El auto se movio {distancia} KM")
        else:
            print("El auto no tiene suficiente combustible")
            
    def ob_posicion(self):
        return f"Distancia recorrida: {self.posicion} KM \n Combustible restante: {self.tanque.ob_com() } "
    

              
            
tanque_com = Tanque()
auto1= Auto(tanque_com)
print(auto1.ob_posicion())
auto1.mover(10)
print(auto1.ob_posicion())
auto1.mover(1000)
print(auto1.ob_posicion())
auto1.mover(10)
print(auto1.ob_posicion())
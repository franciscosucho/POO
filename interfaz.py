from abc import ABC, abstractmethod

# Interfaz simulada (clase abstracta con solo métodos abstractos)
class Operaciones(ABC):
    
    @abstractmethod
    def sumar(self, a, b):
        pass
    
    @abstractmethod
    def restar(self, a, b):
        pass

# Clase concreta que implementa la interfaz
class Calculadora(Operaciones):
    def sumar(self, a, b):
        return a + b
    
    def restar(self, a, b):
        return a - b

# Uso de la clase concreta
calc = Calculadora()
print(calc.sumar(10, 5))   # 15
print(calc.restar(10, 5))  # 5

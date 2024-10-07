from abc import ABC, abstractmethod

# Clase abstracta Pago
class Pago(ABC):
    @abstractmethod
    def procesar_pago(self):
        pass

# Subclases de Pago
class PagoConTarjeta(Pago):
    def procesar_pago(self):
        print("El pago se realizó mediante una tarjeta.")

class PagoConEfectivo(Pago):
    def procesar_pago(self):
        print("El pago se realizó mediante efectivo.")

# Clase Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
    
    def get_nombre(self):
        return self.__nombre
    
    def get_stock(self):
        return self.__stock
    
    def reducir_stock(self, cantidad):
        if self.__stock >= cantidad:
            self.__stock -= cantidad
        else:
            raise Exception("Stock insuficiente.")
    
    def mostrar_info(self):
        return f"Nombre: {self.__nombre}, Precio: {self.__precio}, Stock: {self.__stock}"

# Clase Usuario (base)
class Usuario:
    def __init__(self, nombre, correo):
        self.__nombre = nombre
        self.__correo = correo
    
    def get_nombre(self):
        return self.__nombre

# Clase Cliente heredando de Usuario
class Cliente(Usuario):
    def __init__(self, nombre, correo, direccion):
        super().__init__(nombre, correo)
        self.__direccion = direccion
        self.__pedido = Pedido(self)
    
    def ver_pedido(self):
        print(f"El cliente {self.get_nombre()} tiene un pedido con los siguientes productos:")
        self.__pedido.mostrar_pedido()

# Clase Pedido con composición de productos
class Pedido:
    def __init__(self, cliente):
        self.__cliente = cliente
        self.__productos = []
    
    def agregar_producto(self, producto, cantidad):
        try:
            producto.reducir_stock(cantidad)
            self.__productos.append((producto, cantidad))
        except Exception as e:
            print(f"Error al agregar el producto: {str(e)}")
    
    def mostrar_pedido(self):
        for producto, cantidad in self.__productos:
            print(f"{producto.mostrar_info()}, Cantidad: {cantidad}")

# Ejemplo de uso
try:
    cliente = Cliente("Juan Pérez", "juan@example.com", "Calle Falsa 123")
    producto1 = Producto("Laptop", 1500, 10)
    producto2 = Producto("Mouse", 20, 5)

    cliente.__pedido.agregar_producto(producto1, 1)  # Agregar 1 laptop
    cliente.__pedido.agregar_producto(producto2, 2)  # Agregar 2 mouse

    cliente.ver_pedido()

    pago = PagoConTarjeta()
    pago.procesar_pago()

except Exception as e:
    print(f"Error: {str(e)}")

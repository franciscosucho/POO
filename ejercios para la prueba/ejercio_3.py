"""
Aquí te dejo un ejercicio similar con las mismas pautas de evaluación que tu ejemplo, pero en un contexto diferente. Este nuevo ejercicio se basa en una gestión de inventario de una tienda y cubre los mismos puntos clave: clases, encapsulamiento, abstracción, herencia, polimorfismo, composición y manejo de excepciones.

Requerimientos:
1-Clases y objetos:

    Crea una clase Producto con atributos como nombre, precio, stock.
    Crea una clase Cliente con atributos como nombre, email, direccion.
    Crea una clase Compra, que contendrá la lista de productos comprados, las cantidades y la fecha de compra.
    Crea una clase Tienda, que permitirá gestionar la lista de productos, clientes y compras.
2-Encapsulamiento:

    Asegúrate de que los atributos de cada clase estén encapsulados utilizando modificadores de acceso (privados).
    Proporciona métodos públicos para acceder y modificar los atributos de manera segura.
3-Abstracción:

    Define una clase abstracta Transaccion que contenga el método abstracto procesar().
    Esta clase no debe poder instanciarse directamente, pero deberá ser implementada por las clases hijas.
    Implementa dos clases que hereden de Transaccion: CompraProducto y DevolucionProducto, que deberán definir su forma específica de procesar la compra o la devolución de un producto.
4-Herencia:

    Crea una clase Persona, que servirá como base para la clase Cliente. El cliente heredará atributos como nombre y email.
5-Polimorfismo:

    Implementa el método procesar() de forma polimórfica. Dependiendo del tipo de transacción (compra o devolución), el método deberá comportarse de manera diferente.
6-Composición:

    Una compra tendrá una composición de varios productos. La clase Compra debe contener una lista de productos con las respectivas cantidades y la fecha de compra.
7-Excepciones:

    Implementa un manejo de excepciones para situaciones como intentar realizar una compra con un producto que no tiene stock o intentar devolver un producto que no fue comprado.
"""
from abc import ABC, abstractmethod


class Producto_sin_stock(Exception):
    def __init__(self, message="No hay suficiente stock para realizar la compra"):
        self.message = message
        super().__init__(self.message)

class Producto_no_comprado(Exception):
    def __init__(self, message="Este Producto no fue Comprado y no se puede devolver"):
        self.message = message
        super().__init__(self.message)


class Transaccion(ABC):
    @abstractmethod
    def procesar(self):
        pass

class CompraProducto(Transaccion):
    def procesar(self, producto, cantidad=1):
        if producto.get_stock() < cantidad:
            raise Producto_sin_stock()
        else:
            producto.set_stock(producto.get_stock() - cantidad)



class DevolucionProducto(Transaccion):
    def procesar(self,producto,Compra):
       if producto not in Compra.obtener_lista():
           raise Producto_no_comprado()
       else:
            print(f"Procesando devolución de {producto.get_titulo()}")
            producto.set_stock(producto.get_stock() + 1)  # Aumentar el stock después de la devolución

class Producto():
    def __init__(self,nombre,precio,stock) :
       self.__nombre=nombre
       self.__precio=precio
       self.__stock=stock
    def get_nombre(self):
        return self.__nombre
    def get_precio(self):
        return self.__precio
    def get_stock(self):
        return self.__stock
    def set_stock(self,stock):
       self.__stock = stock
       print(f"Nuevo stock de:",self.__stock)



class Persona():
    def __init__(self,nombre,email) :
        self.__nombre=nombre
        self.__email=email
    def get_nombre(self):
        return  self.__nombre
    def get_email(self):
        return  self.__email

class Cliente(Persona):
    def __init__(self, nombre, email,direccion):
        super().__init__(nombre, email)
        self.__direccion=direccion
    def get_direccion(self):
        return self.__direccion
    
class Compra():
    def __init__(self) :
        self.__productos=[]
        self.__fecha=[]
    def agregar_producto(self,fecha,producto):
        self.__productos.append(producto)
        self.__fecha.append(fecha)
        print(f"Agregando el producto:",producto,",Fecha:",fecha)

    def obtener_lista(self):
        return self.__productos
    def ver_lista(self):
        for i, producto in enumerate(self.__productos):
            print(f"Producto: {producto.get_nombre()}, Fecha de devolución: {self.__fecha[i]}")
tienda_compra=Compra()
Producto1=Producto('pepsi 1L',400,3)
Producto2=Producto('coca 1L',500,0)
try:
    cajera = CompraProducto()
    cajera.procesar(Producto1)  
    tienda_compra.agregar_producto(Producto1, "2024-12-01")
except Producto_sin_stock as e:
        print(e)

    
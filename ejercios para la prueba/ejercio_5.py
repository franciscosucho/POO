"""Requerimientos:

1-Clases y objetos:

    Crea una clase Libro con atributos como titulo, autor, precio, stock.
    Crea una clase Usuario con atributos como nombre, email, dirección.
    Crea una clase Prestamo, que contendrá la lista de libros prestados y la fecha de devolución.
    Crea una clase Biblioteca, que permitirá gestionar la lista de libros, usuarios y préstamos.
2-Encapsulamiento:

    Asegúrate de que los atributos de cada clase estén encapsulados utilizando modificadores de acceso (privados).
    Proporciona métodos públicos para acceder y modificar los atributos de manera segura.
3-Abstracción:

    Define una clase abstracta Transaccion que contenga el método abstracto procesar().
    Esta clase no debe poder instanciarse directamente, pero deberá ser implementada por las clases hijas.
    Implementa dos clases que hereden de Transaccion: PrestamoLibro y DevolucionLibro, que deberán definir su forma específica de procesar el préstamo o la devolución de un libro.
4-Herencia:

    Crea una clase Miembro, que servirá como base para la clase Usuario. Los usuarios heredarán atributos como nombre y email.
5-Polimorfismo:

    Implementa el método procesar() de forma polimórfica. Dependiendo del tipo de transacción (préstamo o devolución), el método deberá comportarse de manera diferente.
6-Composición:

    Un préstamo tendrá una composición de varios libros. La clase Prestamo debe contener una lista de libros con las respectivas fechas de devolución.

7-Excepciones:
    Implementa un manejo de excepciones para situaciones como intentar realizar un préstamo con un libro que no tiene stock o intentar devolver un libro que no fue prestado.
""" 
from abc import ABC,abstractmethod

class Procesar(ABC):
    @abstractmethod
    def procesar(self):
        pass
class PrestamoLibro(Procesar):
    def __init__(self,biblioteca,libro) :
        super().__init__()
        self.biblioteca=biblioteca
        self.libro=libro
    def procesar(self):
        libro_pedir=self.biblioteca.get_lista_libros()
       
        if self.libro not in libro_pedir:
            print("El libro no esta en el catalogo")
      
class Libro():
    def __init__(self,titulo,autor,precio,stock):
        self.__titulo=titulo
        self.__autor=autor
        self.__precio=precio
        self.__stock=stock
    def get_titulo(self):
        return self.__titulo
    def get_autor(self):
        return self.__autor
    def get_precio(self):
        return self.__precio
    def get_stock(self):
        return self.__stock
#Herencia     Crea una clase Miembro, que servirá como base para la clase Usuario. Los usuarios heredarán atributos como nombre y email.
class Miembro():
    def __init__(self,nombre,email) :
        self.__nombre=nombre
        self.__email=email
    def get_nombre(self):
        return self.__nombre
    def get_email(self):
        return self.__email
    
class Usuario(Miembro):
    def __init__(self, nombre, email,direccion):
        super().__init__(nombre, email)
        self.__direccion=direccion
    def get_direccion(self):
        return self.__direccion
class Prestamo():
    def __init__(self,libro,fecha):
        self.__libro=libro
        self.__fecha=fecha
    def get_libro(self):
        return self.__libro
    def get_fecha(self):
        return self.__fecha
class Biblioteca():
    # Crea una clase Biblioteca, que permitirá gestionar la lista de libros, usuarios y préstamos.
    def __init__(self):
        self.__lista_libros=[]
        self.__prestamos=[]
        self.__usuarios=[]
    def agregar_libro(self,libro):
        self.__lista_libros.append(libro)
    def agregar_prestamo(self,prestamo):
        self.__prestamos.append(prestamo)
    def agregar_usuario(self,usuario):
        self.__usuarios.append(usuario)
    def get_lista_libros(self):
        return self.__lista_libros
    def get_prestamos(self):
        return self.__prestamos
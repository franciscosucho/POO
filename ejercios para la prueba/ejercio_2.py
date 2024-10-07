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

from abc import ABC, abstractmethod
# Definir excepciones personalizadas
class StockInsuficienteError(Exception):
    def __init__(self, message="No hay suficiente stock para realizar el préstamo"):
        self.message = message
        super().__init__(self.message)

class LibroNoPrestadoError(Exception):
    def __init__(self, message="Este libro no ha sido prestado y no se puede devolver"):
        self.message = message
        super().__init__(self.message)

class Transaccion(ABC):
    @abstractmethod
    def procesar(self):
        pass

class PrestamoLibro(Transaccion):
    def procesar(self, libro):
        if libro.get_stock() <= 0:
            raise StockInsuficienteError()  # Lanzar excepción si no hay stock
        else:
            print(f"Procesando préstamo de {libro.get_titulo()}")
            libro.set_stock(libro.get_stock() - 1)  # Disminuir el stock después del préstamo

class DevolucionLibro(Transaccion):
    def procesar(self, libro, prestamo):
        if libro not in prestamo.obtener_libros_prestados():
            raise LibroNoPrestadoError()  # Lanzar excepción si el libro no fue prestado
        else:
            print(f"Procesando devolución de {libro.get_titulo()}")
            libro.set_stock(libro.get_stock() + 1)  # Aumentar el stock después de la devolución

class Miembro():
    def __init__(self, nombre, email):
        self.__nombre = nombre
        self.__email = email

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email

class Libro():
    def __init__(self, titulo, autor, precio, stock):
        self.__titulo = titulo
        self.__autor = autor
        self.__precio = precio
        self.__stock = stock

    def get_titulo(self):
        return self.__titulo

    def get_stock(self):
        return self.__stock

    def set_stock(self, stock):
        self.__stock = stock

class Prestamo():
    def __init__(self):
        self.__prestamo = []
        self.__fecha = []

    def agregar_libro(self, libro, fecha):
        self.__prestamo.append(libro)
        self.__fecha.append(fecha)

    def obtener_libros_prestados(self):
        return self.__prestamo

    def ver_prestamos(self):
        for i, libro in enumerate(self.__prestamo):
            print(f"Libro: {libro.get_titulo()}, Fecha de devolución: {self.__fecha[i]}")

class Usuario(Miembro):
    def __init__(self, nombre, email, direccion):
        super().__init__(nombre, email)
        self.__direccion = direccion

    def get_direccion(self):
        return self.__direccion

    def ver_usuario(self):
        print(f"Nombre: {self.get_nombre()}, Email: {self.get_email()}, Dirección: {self.get_direccion()}")

# Ejemplo de uso con manejo de excepciones

biblioteca_prestamo = Prestamo()
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 50, 1)  # Stock inicial es 1

# Intentar realizar un préstamo
try:
    prestamo_libro = PrestamoLibro()
    prestamo_libro.procesar(libro1)  # Procesar el préstamo del libro
    biblioteca_prestamo.agregar_libro(libro1, "2024-12-01")
except StockInsuficienteError as e:
    print(e)

# Intentar realizar otro préstamo cuando ya no hay stock
try:
    prestamo_libro.procesar(libro1)
except StockInsuficienteError as e:
    print(e)  # Aquí lanzará la excepción ya que no hay más stock

# Intentar devolver un libro que no fue prestado
try:
    libro2 = Libro("Don Quijote", "Miguel de Cervantes", 80, 5)  # Libro no prestado
    devolucion_libro = DevolucionLibro()
    devolucion_libro.procesar(libro2, biblioteca_prestamo)
except LibroNoPrestadoError as e:
    print(e)  # Aquí lanzará la excepción ya que el libro no fue prestado

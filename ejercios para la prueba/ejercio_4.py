"""
Ejercicio: Gestión de Reservas en un Hotel
Requerimientos:
1. Clases y Objetos:
    -Crea una clase Habitacion con atributos como número de habitación, tipo (simple, doble, suite) y disponibilidad (True/False).
    -Crea una clase Huesped con atributos como nombre, email y teléfono.
    -Crea una clase Reserva, que contendrá la habitación reservada, el huésped, la fecha de check-in y check-out.
    -Crea una clase Hotel, que permitirá gestionar la lista de habitaciones, huéspedes y reservas.
2. Encapsulamiento:
    -Encapsula los atributos de cada clase utilizando modificadores de acceso privados (__).
    -Proporciona métodos públicos para acceder y modificar los atributos de manera controlada.
3. Abstracción:
    -Define una clase abstracta OperacionHotel que contenga el método abstracto realizar_operacion().
    Esta clase no puede instanciarse directamente, pero debe ser implementada por clases hijas.
4. Herencia:
    -Crea una clase Persona, que servirá como base para la clase Huesped, heredando atributos como nombre y email.
5. Polimorfismo:
    -Implementa el método realizar_operacion() de forma polimórfica en las clases ReservaHabitacion y CancelarReserva. Dependiendo de si es una reserva o cancelación, el método deberá comportarse de manera diferente.
6. Composición:
    -Una reserva debe ser la composición de un huésped y una habitación. La clase Reserva debe contener estos objetos, junto con las fechas de check-in y check-out.
7. Excepciones:
     -un manejo de excepciones para situaciones como intentar reservar una habitación que ya está ocupada o cancelar una reserva inexistente.
"""



from abc import ABC, abstractmethod
class Hotel:
    def __init__(self):
        self.reservas = []
        self.habitaciones = []

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)

    def eliminar_reserva(self, reserva):
        self.reservas.remove(reserva)
    
    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
        
class OperacionHotel(ABC):
    @abstractmethod
    def realizar_operacion(self):
        pass
class ReservaHabitacion(OperacionHotel):
    def __init__(self, reserva):
        self.reserva = reserva
    def realizar_operacion(self, hotel):
        habitacion = self.reserva.get_habitacion()
        if habitacion.get_dispo():
            print(f"Reservando habitación {habitacion.get_numero()}...")
            habitacion.__dispo = False  # Cambia la disponibilidad
            hotel.agregar_reserva(self.reserva)
            print(f"Reserva realizada para el huésped {self.reserva.get_huesped().get_nombre()}")
        else:
            raise Exception("La habitación ya está ocupada")
    
class CancelarReserva(OperacionHotel):
    def __init__(self, reserva):
        self.reserva = reserva

    def realizar_operacion(self, hotel):
        print(f"Cancelando la reserva de la habitación {self.reserva.get_habitacion().get_numero()}...")
        habitacion = self.reserva.get_habitacion()
        habitacion.__dispo = True  # Cambia la disponibilidad
        hotel.eliminar_reserva(self.reserva)
        print(f"Reserva cancelada para el huésped {self.reserva.get_huesped().get_nombre()}")
    
class Habitacion():
    def __init__(self,numero,tipo,dispo) :
            self.__numero = numero
            self.__tipo = tipo
            self.__dispo = dispo
    def get_numero(self):
        return self.__numero
    def get_tipo(self):
        return self.__tipo
    def get_dispo(self):
        return self.__dispo
    
class Persona():
    def __init__(self,nombre,email):
        self.__nombre=nombre
        self.__email=email
    def get_nombre(self):
        return self.__nombre
    def get_email(self):
        return self.__email
class Huesped(Persona):
    def __init__(self, nombre, email,telefono):
        super().__init__(nombre, email)
        self.__telefono = telefono
    def get_telefono(self):
        return self.__telefono
    
class Reserva():
   
    def __init__(self,habitacion_reser,huesped_reser,check_in,check_out):
        self.__habitacion_reser=habitacion_reser
        self.__huesped_reser=huesped_reser
        self.__check_in=check_in
        self.__check_out=check_out
    def get_huesped(self):
        return self.__huesped_reser
    def get_habitacion(self):
        return self.__habitacion_reser
    def get_check_in(self):
        return self.__check_in
    def get_check_out(self):
        return self.__check_out
    def info_reserva(self):
        print(f"Informacion de la reserva: ","Habitacion:",self.get_habitacion,",Huesped:",self.get_huesped,",Check_in:",self.get_check_in,",Check_out:",self.__check_out)
        
# Crear hotel, habitaciones, y huespedes
hotel = Hotel()
habitacion1 = Habitacion(101, "doble", True)
hotel.agregar_habitacion(habitacion1)
huesped1 = Huesped("Juan Pérez", "juan@mail.com", "123456789")

# Crear reserva
reserva1 = Reserva(habitacion1, huesped1, "2024-10-10", "2024-10-15")

# Realizar una operación de reserva
operacion_reserva = ReservaHabitacion(reserva1)
operacion_reserva.realizar_operacion(hotel)

# Cancelar la reserva
operacion_cancelacion = CancelarReserva(reserva1)
operacion_cancelacion.realizar_operacion(hotel)
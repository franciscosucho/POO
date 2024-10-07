class Empleado:

    def __init__(self,nombre):
        self.nombre=nombre
        self.ventas = []

    def agregar_venta(self,id_ven,articulo,fecha):
        venta = Venta(id_ven,articulo, fecha)
        self.ventas.append(venta)

    def mostrar_venta(self):
        print(f"Vendedor: {self.nombre}")
        for venta in self.ventas:
            print(venta.mostrar_info())

class Venta:
    def __init__(self,id_ven,articulo,fecha):
        self.id_ven=id_ven
        self.articulo=articulo
        self.fecha=fecha

    def mostrar_info(self):
        return f"Informacion de la venta: Articulo: {self.articulo},ID: {self.id_ven}, fecha: {self.fecha}"

empleado1= Empleado("Fran Sucho")
empleado1.agregar_venta(1,"articulo 1","08/09/24")
empleado1.agregar_venta(2,"articulo 2","08/09/24")
empleado1.agregar_venta(3,"articulo 3","08/09/24")
empleado1.mostrar_venta()
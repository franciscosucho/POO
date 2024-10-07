class Empleado:
    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto

    def mostrar_info(self):
        return f"Empleado: {self.nombre}, Puesto: {self.puesto}"

class Departamento:
    def __init__(self, nombre_depto):
        self.nombre_depto = nombre_depto
        self.empleados = []  # Los empleados son parte del departamento

    def agregar_empleado(self, nombre, puesto):
        empleado = Empleado(nombre, puesto)
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        print(f"Departamento: {self.nombre_depto}")
        for empleado in self.empleados:
            print(empleado.mostrar_info())

# Ejemplo de uso
depto_rrhh = Departamento("Recursos Humanos")
depto_rrhh.agregar_empleado("Ana Perez", "Gerente de RRHH")
depto_rrhh.agregar_empleado("Carlos Lopez", "Especialista en Reclutamiento")

depto_rrhh.mostrar_empleados()